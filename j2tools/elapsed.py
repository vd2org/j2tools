# Copyright (C) 2017-2019 by Vd.
# This file is part of j2tools package.
# j2tools is released under the MIT License (see LICENSE).


from datetime import datetime


def elapsed(from_time: datetime, *, show_seconds: bool = False, to_time: datetime = None,
            d: str = 'd', h: str = 'h', m: str = 'm', s: str = 's'):
    to_time = to_time if to_time else datetime.utcnow()
    delta = to_time - from_time

    days = delta.days
    seconds = delta.seconds
    hours = delta.seconds // 60 // 60
    seconds = seconds - hours * 60 * 60
    minutes = seconds // 60
    seconds = seconds - minutes * 60

    result = list()

    if days:
        result.append("%d%s" % (days, d))
    if hours or days:
        result.append("%02.0f%s" % (hours, h))

    result.append("%02.0f%s" % (minutes, m))

    if show_seconds:
        result.append("%02.0f%s" % (seconds, s))

    return " ".join(result)


def remaining(to_time: datetime, *, show_seconds: bool = False, from_time: datetime = None,
              d: str = 'd', h: str = 'h', m: str = 'm', s: str = 's'):
    from_time = from_time if from_time else datetime.utcnow()
    return elapsed(from_time, show_seconds=show_seconds, to_time=to_time, d=d, h=h, m=m, s=s)
