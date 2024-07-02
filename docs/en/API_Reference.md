# QuecPython Enhanced Time & TimeZone API Reference Manual

QuecPython Enhanced time and time zone is based on utime and RTC, the functionality is more comprehensive, users can call the utimeextend class, directly use the class method for time and time zone operations.

## Get local time

### `utimeextend.localtime`

```python
utimeextend.localtime(timestamp=None, tz=None)
```

**Parameters**

- `timestamp` - int,Optional: Enter the timestamp. Otherwise, the current RTC time is directly displayed
- `tz` - int/float,Optional: Time zone, the value ranges from -12 to 14. The time calculated by the timestamp is plus the time zone offset. If this parameter is not specified, the GMT time is displayed by default

**Return Value**

Returns a tuple of the format (year, month, day, hour, minute, second, weekday, yearday).

## Set loacl time

### `utimeextend.setlocaltime`

```python
utimeextend.setlocaltime(tm_tuple)
```

**Parameters**

- `tm_tuple` - tuple(year, month, day, hour, minute, second, weekday, yearday):设置时间

**Return Value**

int:0 for success, else for failure

## Set Time Zone

### `utimeextend.setTimeZone`

```python
utimeextend.setTimeZone(tz)
```
**Parameters**

- `tz` - int,time zone,range -12~14。

**Return Value**

int:0 for success, else for failure

## Get Time Zone

### `utimeextend.getTimeZone`

```python
utimeextend.getTimeZone()
```

**Return Value**

int: Time Zone

## Set Time Zone(Enhanced, support float)

### `utimeextend.setTimeZoneEx`

```python
utimeextend.setTimeZoneEx(tz)
```

**Parameters**

- `tz` - float,time zone,range -12.0~14.0。

**Return Value**

int:0 for success, else for failure

> - To use the enhanced time zone interface Settings, you must use the enhanced time zone interface to obtain, otherwise it will cause precision loss

## Get Time Zone(Enhanced, support float)

### `utimeextend.getTimeZoneEx`

```python
utimeextend.getTimeZoneEx()
```

**Return Value**

float: Time Zone

> - To use the enhanced time zone interface Settings, you must use the enhanced time zone interface to obtain, otherwise it will cause precision loss