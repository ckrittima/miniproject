from django import template
from datetime import datetime

register = template.Library()

@register.filter
def time_in_range(start, end):
    """Return true if x is in the range [start, end]"""
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_time = datetime.strptime(current_time, '%H:%M:%S').time()
    # start = datetime.strptime(str(start), '%H:%M:%S').time()
    # end = datetime.strptime(str(end), '%H:%M:%S').time()
    print(start)
    if start <= end:
        return start <= current_time <= end
    else:
        return start <= current_time or current_time <= end

