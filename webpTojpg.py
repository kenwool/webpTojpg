from PIL import Image
import os

# 获取当前文件夹中所有的webp格式图片
webp_files = [f for f in os.listdir() if f.endswith('.webp')]

# 遍历每个webp文件并将其转换为jpg格式
for webp_file in webp_files:
    # 打开webp图片
    with Image.open(webp_file) as img:
        # 构造输出的jpg文件名，将webp扩展名替换为jpg
        jpg_file = webp_file.replace('.webp', '.jpg')
        # 保存为jpg格式，quality=100表示无损保存
        img.save(jpg_file, 'JPEG', quality=100)

print("转换完成！")
