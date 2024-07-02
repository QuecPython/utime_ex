# QuecPython 增强型时间和时区 API 参考手册

QuecPython 增强型时间和时区是基于utime和RTC，实现的功能更为全面，用户可以在调用utimeextend类，直接使用类方法进行时间和时区操作。


## 获取本地时间

### `utimeextend.localtime`

```python
utimeextend.localtime(timestamp=None, tz=None)
```

**参数**

- `timestamp` - int,可选，输入时间戳，否则直接输出当前RTC时间
- `tz` - int/float,可选，时区，范围-12~14,可使时间戳解算的时间加时区偏移,不填此参数则默认输出GMT时间

**返回值**

返回元组，格式为(year, month, day, hour, minute, second, weekday, yearday)


## 设置本地时间

### `utimeextend.setlocaltime`

```python
utimeextend.setlocaltime(tm_tuple)
```

**参数**

- `tm_tuple` - tuple(year, month, day, hour, minute, second, weekday, yearday):设置时间

**返回值**

int:0设置成功,否则失败


## 设置时区

### `utimeextend.setTimeZone`

```python
utimeextend.setTimeZone(tz)
```

**参数**

- `tz` - int,时区,范围-12~14。

**返回值**

int:0设置成功,否则失败


## 获取时区

### `utimeextend.getTimeZone`

```python
utimeextend.getTimeZone()
```

**返回值**

int:时区


## 设置时区(增强型,支持浮点)

### `utimeextend.setTimeZoneEx`

```python
utimeextend.setTimeZoneEx(tz)
```
**参数**

- `tz` - float,时区,范围-12.0~14.0

**返回值**

int:0设置成功,否则失败

> - 使用增强型时区接口设置，就要用增强型时区接口获取，否则会造成精度丢失

## 获取时区(增强型,支持浮点)

### `utimeextend.getTimeZoneEx`

```python
utimeextend.getTimeZoneEx()
```
**返回值**

float:时区

> - 使用增强型时区接口设置，就要用增强型时区接口获取，否则会造成精度丢失

