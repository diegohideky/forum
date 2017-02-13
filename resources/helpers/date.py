#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime


def now():
    return datetime.datetime.now()


def today():
    return datetime.date.today()


def dateFormat(dd, mm, yy):
    return datetime.date(int(yy), int(mm), int(dd))


def timeFormat(time):
    return datetime.datetime.strptime(time, "%H:%M").time()

