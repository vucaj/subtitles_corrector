import pysrt

SUBTITLE_PATH = '../Desktop/The.Grand.Tour.S04E02.WEBRip.x264-ION10.srt'
NEW_SUBTITLE_PATH = '../Desktop/Converted.Subtitles.srt'


def write_file(subs):
    file = open(NEW_SUBTITLE_PATH, 'wb')
    for i in range(len(subs)):
        file.write(subs[i].encode('utf-8'))

    file.close()


def convert_letters(subs):
    retVal = []
    iter = 1
    for sub in subs:
        retVal.append(str(iter) + '\n')
        retVal.append(str(sub.start) + ' --> ' + str(sub.end) + '\n')
        text = sub.text
        text = text.replace('È', 'Č')
        text = text.replace('è', 'č')
        text = text.replace('æ', 'ć')
        text = text.replace('ð', 'đ')
        text = text.replace('', 'ž')
        text = text.replace('', 'Ž')
        text = text.replace('', 'š')
        text = text.replace('', 'Š')

        retVal.append(text + '\n\n')
        iter += 1

    return retVal


if __name__ == '__main__':
    subs = pysrt.open(SUBTITLE_PATH, encoding='iso-8859-1')
    converted_subs = convert_letters(subs)
    write_file(converted_subs)