# EXG社区资源包替换脚本

## Usage

下载以下这个7z和7z插件，在7z文件目录中新建一个名为`format`的文件夹，并把dll文件复制进去

`https://github.com/SCell555/7-Zip-zstd`
`https://github.com/SCell555/7zip-vpk?tab=readme-ov-file`

使用7z把资源包解压

找到想要替换的模型，并移动到资源包文件夹外面，如果要换成鸡哥目录在`characters\models\normal\normal.vmdl_c`

运行脚本，例如`python main.py --path 'C:\Users\233kun\Desktop\exg_resources' --source 'C:\Users\233kun\normal.vmdl_c'`

参数注解
- --path 解压后资源包目录
- --source 要替换的模型
- --exceptions 不替换的模型

最后将资源包打包，记得分卷，因为V社限制资源包最大3G