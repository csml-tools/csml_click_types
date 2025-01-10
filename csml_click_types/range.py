from typing import Any, Optional
import click


class RangeParamType(click.ParamType):
    def convert(
        self, value: Any, param: Optional[click.Parameter], ctx: Optional[click.Context]
    ) -> Any:
        if isinstance(value, range):
            return value
        elif isinstance(value, str):
            parts = value.split("-")

            if len(parts) == 2:
                return range(int(parts[0]), int(parts[1]) + 1)
            elif len(parts) == 1:
                num = int(parts[0])
                return range(num, num + 1)
            else:
                self.fail(
                    f"{value} is not a range string, expected format like '0-100'",
                    param,
                    ctx,
                )
        else:
            self.fail("Must be str or range", param, ctx)


range_param_type = RangeParamType()

__all__ = ["RangeParamType", "range_param_type"]
