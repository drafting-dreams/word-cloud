
#coding=utf-8


#导入wordcloud模块和matplotlib模块
from wordcloud import WordCloud,ImageColorGenerator
import  matplotlib.pyplot as plt
from scipy.misc import imread
import jieba
import jieba.analyse
import sys

file_name = sys.argv[1][1:]
prefix = sys.argv[1][0]
# print(file_name)
# print('a')
content = open(file_name,"rb").read()
tags = jieba.analyse.extract_tags(content, topK=100, withWeight=False)
text =" ".join(tags)
# print(text)
# text = unicode(text)

#读入背景图片
bj_pic=imread('.\\bg.png')

#生成词云（通常字体路径均设置在C:\\Windows\\Fonts\\也可自行下载）
font=r'C:\\Windows\\Fonts\\STFANGSO.ttf'#不加这一句显示口字形乱码  ""报错
wordcloud=WordCloud(mask=bj_pic,background_color='white',font_path=font,scale=3.5).generate(text)
  #img_color = ImageColorGenerator(self.img)
image_colors=ImageColorGenerator(bj_pic)
#显示词云

# plt.imshow(wordcloud)
# plt.axis('off')
# plt.show()
output_name = prefix+file_name.split('.')[0]+'.jpg'
print(output_name.encode('utf-8'))
wordcloud.to_file('.\\dist\\'+output_name)
