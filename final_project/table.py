#!/bin/python3
############################################
# DATE : 2024-10-14                        #
# AUTH : Isaac Palmersheim                 #
# DESC : A class to format data to a table #
############################################

###########
# Imports #
###########
from typing import Iterable
import datetime


class Table:
    """
    Table formatting engine with custom datatype support!

    Arguments
    columnNames : list of strings containing the headers for each column
    data : a multi-dimensional array containing each row to be formatted
    vertical : the character to be used for vertical lines
    horizontal : the character to be used for horizontal lines
    corner : the character to be used for corners
    """

    """
    Formatting driver system
    structure:
    {
        '<class_name>': (
            <size calculator>
            1 argument
            data : The data to be formatted
            <f-string generator>
            2 arguments
            data : The data to be formatted
            length : The alloted size for the string
        )
    }
    """
    FORMAT_DRIVERS = {
        "str": (
            lambda data: len(str(data)),
            lambda data, size: f"{str(data):{size}s}"
        ),
        "int": (
            lambda data: len(f"{data:,d}"),
            lambda data, size: f"{data:{size},d}"
        ),
        "bool": (
            lambda data: 3 if data else 2,
            lambda data, size: f"{'Yes':{size}s}" if data else f"{'No':{size}s}"
        ),
        "float": (
            lambda data: len(str(round(data, 2))),
            lambda data, size: f"{data:{size}.2f}"
        ),
        "datetime": (
            lambda data: len(data.strftime("%Y-%m-%d")),
            lambda data, size: f"{data.strftime('%Y-%m-%d'):>{size}s}"
        ),
    }

    ###################
    # Magic Functions #
    ###################
    def __init__(
            self,
            columnNames: list | tuple,
            data: list | tuple,
            vertical: str = "|",
            horizontal: str = "-",
            corner: str = "+"
    ) -> None:
        max_width = 184
        ##################
        # Initialization #
        ##################
        self._columns = columnNames
        self._rows = data
        self._vert = vertical
        self._horiz = horizontal
        self._corner = corner
        self._width = max_width
        self._min_width = sum([len(_) + 3 for _ in columnNames]) + 1

        #########################
        # Argument Sanitization #
        #########################
        if err := self._sanitize_column_names(columnNames):
            raise err
        if err := self._sanitize_rows(data, len(columnNames)):
            raise err
        if err := self._sanitize_characters(vertical, horizontal, corner):
            raise err
        if err := self._sanitize_size(max_width, self._min_width):
            raise err

        ##################
        # Custom Drivers #
        ##################
        self._drivers = {}

    def __str__(
            self
    ) -> str:
        """
        Generates table to be printed
        """
        #############
        # Variables #
        #############
        # Driver table merged from custom drivers table
        drivers = {**Table.FORMAT_DRIVERS, **self._drivers}
        # Size allocation for each column
        row_sizes = self._compute_row_sizes(
            [self._columns] + self._rows,
            drivers
        )
        # Total table size
        total_size = sum(row_sizes) + len(row_sizes) * 3
        # Generation results
        result = ""
        errs = []

        ###########
        # Heading #
        ###########
        # Add top line
        result += f"{self._corner}{self._horiz * total_size}{self._corner}\n"
        # Add columns
        for cnt, col in enumerate(self._columns):
            result += f"{self._vert} {col:^{row_sizes[cnt]}s} "
        # Add line break
        result += f" {self._vert}\n"

        ########
        # Body #
        ########
        for row in self._rows:
            # Add top line
            result += f"{self._corner}{self._horiz * total_size}{self._corner}\n"

            for cnt, col in enumerate(row):
                # Fetch driver for datatype
                dtype = type(col).__name__
                driver = drivers.get(dtype)
                # If no driver exists, default with string driver
                if not driver:
                    driver = Table.FORMAT_DRIVERS["str"]

                # Attempt to format with driver        
                try:
                    result += f"{self._vert} {driver[1](col, row_sizes[cnt])} "
                # If driver fails, log to list and indicate in table
                except Exception as e:
                    result += f"{self._vert} {'E' + str(len(errs)):{row_sizes[cnt]}s} "
                    errs.append((dtype, col, err))

            # Add line break
            result += f" {self._vert}\n"

        # Add final line
        result += f"{self._corner}{self._horiz * total_size}{self._corner}\n"

        # Output errors (if any)
        for err in errs:
            print(f"ERROR CAUGHT! Driver for {err[0]} threw an error when processing {err[1]}.")
            print(err[2])
        return result

    def __repr__(
            self
    ) -> str:
        """
        Mirrors __str__
        """
        return self.__str__()

    ######################
    # External Functions #
    ######################
    def AppendRow(
            self,
            row: list
    ) -> None:
        """
        Adds a row to the end of the list
        """
        if len(row) != len(self._columns):
            raise ValueError(
                f"Length of row in given data is not equal to number of columns! Expected length of {len(self._columns)} but got length {len(row)}!")
        self._rows.append(
            row
        )

    def PrependRow(
            self,
            row: list
    ) -> None:
        """
        Adds a row to the beginning of the list
        """
        if len(row) != len(self._columns):
            raise ValueError(
                f"Length of row in given data is not equal to number of columns! Expected length of {len(self._columns)} but got length {len(row)}!")
        self._rows = (
                row +
                self._rows
        )

    def AddDriver(
            self,
            datatype: str,
            length,
            formatter
    ) -> None:
        """

        Adds/Overwrites formatting driver to table generator

        !!! WARNING !!!
        No checks are done to ensure the driver
        A) Functions properly
        B) Does not break the default drivers
        C) Is not malicious or secure by any means

        When in doubt, refer to the FORMAT_DRIVERS table at
        the top of the class definition to see how the default
        drivers work and should behave.

        The engine will attempt to catch any errors created
        by any custom drivers and attempt to recover from
        said error. Any errors will be printed above the table
        for review.
        """
        self._drivers[datatype.__name__] = (
            length,
            formatter
        )

    ######################
    # Internal Functions #
    ######################
    # Sanitization Functions
    def _sanitize_column_names(
            self,
            columnNames: list | tuple
    ) -> Exception | None:
        """
        Sanitizes all column names to ensure appropriate type
        """
        for col in columnNames:
            if type(col) != str:
                return ValueError(
                    f"A column in argument \'columnNames\' contains a non-string value. Expected {type('text')} but got {type(col)}!")

    def _sanitize_rows(
            self,
            rows: list | tuple,
            colCount: int
    ) -> Exception | None:
        """
        Sanitizes the given data rows to ensure appropriate length and types
        """
        for row in rows:
            if not (
                    type(row) == list
                    or
                    type(row) == tuple
            ):
                return ValueError(
                    f"A row in argument \'data\' is not of type \'list\' or \'tuple\'! Expected {list} or {tuple} but got {type(row)}!")
            if len(row) != colCount:
                return ValueError(
                    f"Length of row in given data is not equal to number of columns! Expected length of {colCount} but got length {len(row)}!")

    def _sanitize_characters(
            self,
            vertical: str,
            horizontal: str,
            corner: str
    ) -> Exception | None:
        """
        Sanitizes the given strings for drawing the table
        """
        if len(vertical) != 1:
            return ValueError(f"Argument \'vertical\' is not a single character!")
        if len(horizontal) != 1:
            return ValueError(f"Argument \'horizontal\' is not a single character!")
        if len(corner) != 1:
            return ValueError(f"Argument \'corner\' is not a single character!")

    def _sanitize_size(
            self,
            maxWidth: int,
            minWidth: int
    ) -> Exception | None:
        """
        Sanitizes the given size input
        """
        if maxWidth < 0:
            return ValueError(f"Argument \'max_width\' cannot be negative!")
        if maxWidth < minWidth:
            return ValueError(
                f"Argument \'max_width\' cannot be less than the minimum possible size for the table! Expected a number larger than {minWidth} but got {maxWidth}!")

    # Helper Functions
    def _compute_row_sizes(
            self,
            rows: list,
            drivers: dict
    ) -> list:
        """
        Computes the formatting sizes from a given array
        """
        maximum = [0 for _ in rows[0]]
        for row in rows:
            for cnt, col in enumerate(row):
                # Attempt to load and use associated driver
                try:
                    if driver := drivers.get(
                            type(col).__name__
                    ): size = driver[0](col)
                # Use string driver as fallback
                except:
                    if driver := drivers.get("str"):
                        size = driver[0](col)
                    # Set size to zero if all else fails
                    else:
                        size = 0
                if size > maximum[cnt]:
                    maximum[cnt] = size
        return maximum


class ID:
    def __init__(
            self,
            id: int
    ): self.id = id


def print_table(
        table_data: list
) -> None:
    tmp = Table(
        table_data[0],
        table_data[1:]
    )
    tmp.AddDriver(
        type(ID(0)),
        lambda data: len(str(data.id)),
        lambda data, size: f"{data.id:{size}d}"
    )
    print(tmp)


if __name__ == "__main__":
    print_table(
        [
            ["ID", "Name", "Student", "GPA", "Salary", "Hired"],
            [ID(101), "Marc Hauschildt", False, 3.1, 85000, datetime.datetime(2020, 8, 1)],
            [ID(1001), "Isaac Palmersheim", True, 3.99, 100000, datetime.datetime(2024, 10, 1)],
            [ID(69), "Gerald Williams", True, 0.69, 25000, datetime.datetime(1999, 4, 7)],
            [ID(10002), "Bruce Wayne", False, 4.0, 1250000, datetime.datetime(2001, 2, 19)]
        ]
    )
    print_table(
        [
            ["SSN", "Income", "Expenses", "Has Paid", "Marial Status"],
            [1, 250000, 12500, False, "Single"],
            [2, 45000, 1000, True, "Married"],
            [3, 1000000, 300000, False, "Single"],
        ]
    )