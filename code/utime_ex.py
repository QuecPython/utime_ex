'''
背景:标准的UTC时区应为-12到+12,但某些国境横跨国际日期变更线的国家为保持全国日期统一,将
原属UTC-11的领土日期前推一天,即从UTC-11加24H,是为UTC+13
'''
import utime
from machine import RTC

class utimeextend(object):
    #如果设置的时区大于UTC+12,此flag被置为True
    isExtendTz = False
    
    """_extend_tz_handle
        内部函数,在使用扩展时区(isExtendTz = False = True)时处理时间,将时间前推24h,例如从UTC-11把时间映射到UTC+13

    Returns:
        tuple: (year, month, day, hour, minute, second, weekday, yearday)
    """
    @classmethod
    def _extend_tz_handle(cls):
        tm_temp_in = utime.mktime(utime.localtime())
        tm_tuple_out = utime.localtime(tm_temp_in + (24*60*60))

        return tm_tuple_out

    """localtime
        扩展原生utime的方法,不带参数时,如果isExtendTz = True,此时输出的时间应为模组的RTC时间加偏24H.
        带参数时由传入的时间戳解算出时间
    args:
        args[0]:int,时间戳,单位s
        args[1]:int,时区,范围-12~14,可使时间戳解算的时间加时区偏移,不填此参数则默认输出GMT时间

    Returns:
        tuple(year, month, day, hour, minute, second, weekday, yearday):返回时间
     """
    @classmethod
    def localtime(cls, *args):
        tm_tuple = ()
        if not args:
            tm_tuple = cls._extend_tz_handle() if cls.isExtendTz else utime.localtime()

        elif len(args) == 1:
            tm_tuple = utime.localtime(args[0] - (8*60*60))

        elif len(args) == 2:
            tm_tuple = utime.localtime(args[0] - (8*60*60) + (args[1]*60*60))

        else:
            raise(ValueError, "Arguments Error")    
        
        return tm_tuple

    '''setTimeZoneEx
        设置时区(增强型,支持浮点)
        如果设置的时区大于UTC+12且小于等于UTC+14,此时向模组中设入此时区对应的标准UTC时区(如UTC+13 -> UTC-11),并将isExtendTz置为True
        如果在标准时区之内,则直接使用模组底层时区
    args:
        tz:float,时区,范围-12.0~14.0

    Returns:
        int:0设置成功,否则失败      
    '''
    @classmethod
    def setTimeZoneEx(cls, tz):
        if 12.0 < tz <= 14.0 :
            cls.isExtendTz = True
            return utime.setTimeZoneEx(tz - 24.0)
        else :
            cls.isExtendTz = False
            return utime.setTimeZoneEx(tz)

    '''getTimeZoneEx
        获取时区(增强型,支持浮点)
        如果isExtendTz = True,从模组对应的时区应加24小时
    Returns:
        float:时区    
    '''
    @classmethod       
    def getTimeZoneEx(cls):
        if cls.isExtendTz :
            return utime.getTimeZoneEx() + 24.0
        else :
            return utime.getTimeZoneEx()

    '''setTimeZone
        设置时区
        如果设置的时区大于UTC+12且小于等于UTC+14,此时向模组中设入此时区对应的标准UTC时区(如UTC+13 -> UTC-11),并将isExtendTz置为True
        如果在标准时区之内,则直接使用模组底层时区
    args:
        tz:int,时区

    Returns:
        int:0设置成功,否则失败      
    '''
    @classmethod
    def setTimeZone(cls, tz):
        if 12 < tz <= 14 :
            cls.isExtendTz = True
            return utime.setTimeZone(int(tz - 24))
        else :
            cls.isExtendTz = False
            return utime.setTimeZone(int(tz))

    '''getTimeZone
        获取时区
        如果isExtendTz = True,从模组对应的时区应加24小时
    Returns:
        int:时区    
    '''
    @classmethod       
    def getTimeZone(cls):
        if cls.isExtendTz :
            return int(utime.getTimeZoneEx() + 24)
        else :
            return int(utime.getTimeZoneEx())    

    '''setlocaltime
        设定时间(带时区偏移)&元组转换,解决RTC和localtime存在时区偏移,以及数据格式不同的问题
        所设即所得,自动计算localtime对RTC时间的偏移量,无论在任何条件下,utimeextend.localtime()获取的时间均应符合此接口设置
    args:    
        tm_tuple:tuple(year, month, day, hour, minute, second, weekday, yearday):设置时间

    Returns:
        int:0设置成功,否则失败
    '''        
    @classmethod
    def setlocaltime(cls, tm_tuple):
        temp_rtc = RTC()
        #RTC_datatime_list:[year, month, day, week, hour, minute, second, microsecond]
        try:
            temp_rtc.datetime([tm_tuple[0], tm_tuple[1], tm_tuple[2], tm_tuple[6], tm_tuple[3], tm_tuple[4], tm_tuple[5], 0])
        except:
            raise(TypeError,"Error time argument")

        tm_rtc_in = utime.mktime(tm_tuple)
        offset = tm_rtc_in - utime.mktime(utime.localtime())#此处通过一次尝试设置,计算当前时区配置下RTC时间和localtime的差值

        print(str(offset) + "s for offset\r\n")

        tm_set_tuple = ()
        if not cls.isExtendTz:
            tm_set_tuple = utime.localtime(tm_rtc_in + offset)
        else:
            tm_set_tuple = utime.localtime(tm_rtc_in + offset - (24*60*60))#东十二区以上还要添加到对应标准时区的一天偏差

        return temp_rtc.datetime([tm_set_tuple[0], tm_set_tuple[1], tm_set_tuple[2], tm_set_tuple[6], tm_set_tuple[3], tm_set_tuple[4], tm_set_tuple[5], 0])

    '''mktime
        由时间转换时间戳
    args:    
        tm_tuple_in:tuple(year, month, day, hour, minute, second, weekday, yearday):输入时间
        time_zone:int,时区,不填默认输出GMT时间戳

    Returns:
        int:0设置成功,否则失败
    '''       
    @classmethod
    def mktime(cls, tm_tuple_in, time_zone = 0):

        return utime.mktime(tm_tuple_in) + (8*60*60) - (time_zone*60*60)#UTC timestamp with timezone
    

            
        

