import re


def extract_chinese_sensitive_info(text):
    patterns = {
        '姓名': r'姓名:\s*([^\n]*)',
        '出生日期': r'出生日期:\s*([^\n]*)',
        '身份证号码': r'身份证号码:\s*([^\n]*)',
        '地址': r'地址:\s*([^\n]*)',
        '电话号码': r'电话号码:\s*([^\n]*)',
        '电子邮件': r'电子邮件:\s*([^\n]*)',
        '银行名称': r'银行名称:\s*([^\n]*)',
        '账号': r'账号:\s*([^\n]*)',
        '工作单位': r'工作单位:\s*([^\n]*)',
        '职位': r'职位:\s*([^\n]*)'
    }

    sensitive_info = {}
    for key, pattern in patterns.items():
        match = re.findall(pattern, text)
        if match:
            sensitive_info[key] = match
    return sensitive_info


def redact_chinese_sensitive_info(text):
    patterns = {
        '姓名': r'姓名:\s*([^\n]*)',
        '出生日期': r'出生日期:\s*([^\n]*)',
        '身份证号码': r'身份证号码:\s*([^\n]*)',
        '地址': r'地址:\s*([^\n]*)',
        '电话号码': r'电话号码:\s*([^\n]*)',
        '电子邮件': r'电子邮件:\s*([^\n]*)',
        '银行名称': r'银行名称:\s*([^\n]*)',
        '账号': r'账号:\s*([^\n]*)',
        '工作单位': r'工作单位:\s*([^\n]*)',
        '职位': r'职位:\s*([^\n]*)'
    }

    for key, pattern in patterns.items():
        text = re.sub(pattern, f'{key}: REDACTED', text)
    return text
