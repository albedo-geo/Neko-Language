import base64

__all__ = ['neko_encode', 'neko_decode']

BIN_WIDTH = 7
C0 = "~"
C1 = '喵'


def neko_encode(message: str) -> str:
    """将信息转为喵星语"""

    m_encode = str(base64.b64encode(bytes(message, encoding='utf8')), encoding='ascii')
    # print(f'Base64编码后的结果为：{m_encode}')
    m_binary = ''
    for c in m_encode:
        n = ord(c)
        # 二进制需要定宽，否则无法解码
        b = bin(n)[2:].rjust(BIN_WIDTH, '0')
        # print(c, n, b)
        m_binary += b
    # print(f'二进制为：{m_binary}')
    result = m_binary.replace('1', C1)
    result = result.replace('0', C0)
    return result


def neko_decode(ciphertext: str) -> str:
    """将喵星语转换回原文"""

    # 做一个快速的检查，判断输入的内容是否符合要求
    chars = set(ciphertext)
    if C0 in chars:
        chars.remove(C0)
    if C1 in chars:
        chars.remove(C1)
    if len(chars) > 0:
        return ""

    m_binary = ciphertext.replace(C1, '1')
    m_binary = m_binary.replace(C0, '0')
    m_encode = ''
    for b in [
        m_binary[i : i + BIN_WIDTH]
        for i in range(0, len(m_binary) - BIN_WIDTH + 1, BIN_WIDTH)
    ]:
        n = int(b, base=2)
        c = chr(n)
        # print(b, n, c)
        m_encode += c
    # print(f'编码为：{m_encode}')
    result = base64.b64decode(m_encode)
    return str(result, encoding='utf8')
