from datetime import datetime
import pytz
import jdatetime

def convert_to_tehran_jalali(date_str, original_timezone="UTC", date_format="%a, %d %b %Y %H:%M:%S %z"):
    """
    تبدیل تاریخ و ساعت به وقت تهران و سپس به تاریخ شمسی
    
    :param date_str: رشته تاریخ و ساعت
    :param original_timezone: منطقه زمانی اصلی (پیش‌فرض: UTC)
    :param date_format: قالب تاریخ و ساعت ورودی (پیش‌فرض: RFC 2822)
    :return: تاریخ و ساعت به وقت تهران به صورت شمسی
    """
    # تبدیل رشته تاریخ به شیء datetime با منطقه زمانی اصلی
    original_date = datetime.strptime(date_str, date_format)
    original_date = original_date.replace(tzinfo=pytz.timezone(original_timezone))
    
    # تنظیم منطقه زمانی به وقت تهران
    tehran_timezone = pytz.timezone("Asia/Tehran")
    tehran_date = original_date.astimezone(tehran_timezone)
    
    # تبدیل تاریخ میلادی به تاریخ شمسی
    jalali_date = jdatetime.datetime.fromgregorian(datetime=tehran_date)
    
    # برگرداندن تاریخ شمسی به صورت رشته
    return jalali_date.strftime("%Y-%m-%d %H:%M:%S")
    