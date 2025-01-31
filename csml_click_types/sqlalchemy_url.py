from typing import Any, Optional
import click

import sqlalchemy


class SqlalchemyUrlParamType(click.ParamType):
    name = "url"

    def convert(
        self, value: Any, param: Optional[click.Parameter], ctx: Optional[click.Context]
    ) -> Any:
        if isinstance(value, sqlalchemy.URL):
            return value
        elif isinstance(value, str):
            return sqlalchemy.make_url(value)
        else:
            self.fail("Must be str or sqlalchemy.URL", param, ctx)
