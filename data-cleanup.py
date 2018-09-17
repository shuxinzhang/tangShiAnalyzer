# -*- coding: utf-8 -*-
import json
import io
def merge_json():
    data = []
    for i in range(0,58):
        file_name = "json/poet.tang." + str(i*1000) + '.json'
        try:
            f = io.open(file_name)
            poem_data = json.load(f)
            for poem in poem_data:      
                if (len(poem['paragraphs']) != 0 and poem['author']!='不詳'.decode('utf-8')):
                    temp_poem = {}
                    temp_poem['author'] = poem['author']
                    temp_poem['paragraphs'] = poem['paragraphs']
                    temp_poem['title'] = poem['title']
                    data.append(temp_poem)
            #print(data[i])
        finally:
            f.close()
            print('file processing #' + str(i) +' completed ')
    with io.open('final_data.json','w') as jfile:
        jfile.write(json.dumps(data,ensure_ascii=False,encoding="utf8"))


if __name__ == "__main__":
    merge_json()


