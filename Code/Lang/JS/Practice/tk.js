128 > m ? e[f++] = m : (2048 > m ? e[f++] = m >> 6 | 192 : (55296 == (m & 64512) && g + 1 < a.length && 56320 == (a.charCodeAt(g + 1) & 64512) ? (m = 65536 + ((m & 1023) << 10) + (a.charCodeAt(++g) & 1023), e[f++] = m >> 18 | 240, e[f++] = m >> 12 & 63 | 128) : e[f++] = m >> 12 | 224, e[f++] = m >> 6 & 63 | 128), e[f++] = m & 63 | 128)


if (128 > m) {
    e[f++] = m
} else if (2048 > m) {
    e[f++] = m >> 6 | 192
} else if (55296 == (m & 64512) && g + 1 < a.length && 56320 == (a.charCodeAt(g + 1) & 64512)) {
    m = 65536 + ((m & 1023) << 10) + (a.charCodeAt(++g) & 1023),
    e[f++] = m >> 18 | 240, e[f++] = m >> 12 & 63 | 128
} else {
    e[f++] = m >> 12 | 224
    e[f++] = m >> 6 & 63 | 128
    e[f++] = m & 63 | 128
}