def format_date(date): #= "2023-12-16"
    ele = date.split("-")
    if ele[1]=='01':
        return f"{ele[2]} January, {ele[0]}"
    elif ele[1]=='02':
        return f"{ele[2]} February, {ele[0]}"
    elif ele[1]=='03':
        return f"{ele[2]} March, {ele[0]}"
    elif ele[1]=='04':
        return f"{ele[2]} April, {ele[0]}"
    elif ele[1]=='05':
        return f"{ele[2]} May, {ele[0]}"
    elif ele[1]=='06':
        return f"{ele[2]} June, {ele[0]}"
    elif ele[1]=='07':
        return f"{ele[2]} July, {ele[0]}"
    elif ele[1]=='08':
        return f"{ele[2]} August, {ele[0]}"
    elif ele[1]=='09':
        return f"{ele[2]} September, {ele[0]}"
    elif ele[1]=='10':
        return f"{ele[2]} October, {ele[0]}"
    elif ele[1]=='11':
        return f"{ele[2]} November, {ele[0]}"
    elif ele[1]=='12':
        return f"{ele[2]} December, {ele[0]}"
    
