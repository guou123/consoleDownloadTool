import requests
from tqdm import tqdm
import time
from rich.console import Console
# from rich.panel import Panel

console = Console()
with console.status("[blue]初始化中[/]"):
    for i in range(19):
        time.sleep(0.1)


def download_file(url):
    lk = url.split('.')[-1]
    print("文件类型" + lk)
    file_path = rf"C:\Users\72356\Downloads\d1.{lk}"
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get("content-length"))
    block_size = 1024
    progress_bar = tqdm(total=total_size, unit="B", unit_scale=True)
    with open(file_path, "wb") as f:
        for data in response.iter_content(block_size):
            progress_bar.update(len(data))
            f.write(data)
    progress_bar.close()
    print("文件下载完成")


def main():
    from rich.table import Table
    table = Table()
    table.add_column('[red]欢迎使用我的软件')
    table.add_row('[red]官网:guou123.github.io')
    console.print(table)
    while True:
        console.print("(1)下载文件",end="")
        console.print("(2)退出")
        q = console.input()
        if q == "1":
            console.print("请输入文件链接")
            url = console.input()
            download_file(url)
            console.print("文件已保存到系统下载文件夹")
        elif q == "2":
            break
        else:
            console.print("输入错误")


if __name__ == "__main__":
    main()
