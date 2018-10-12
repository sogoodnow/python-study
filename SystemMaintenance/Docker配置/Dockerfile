# Version:1.0
# 文件开头必须为FROM指定父镜像，可以有多个FROM
FROM alpine:last
# 维护者，非必须，用户名，邮箱
MAINTAINER QIU 'QIU@qq.com'
# 标签1.0 LABEL <key>=<value> <key>=<value> <key>=<value> ...
LABEL version="1.0"
# 描述
LABEL description="fist image"
# 设置后续命令（镜像内）的执行者用户
#USER <user>[:<group>] or
#USER <UID>[:<GID>]
USER root
# 镜像生成后执行命令
#RUN 有两种运行方式
#RUN <command> (shell form, the command is run in a shell, which by default is /bin/sh -c on Linux or cmd /S /C on Windows)
#RUN ["executable", "param1", "param2"] (exec form)
RUN apk update && apk add python3
# 对外暴露端口 EXPOSE <port> [<port>/<protocol>...] 实际使用时会以-p暴露的端口为准 默认为/tcp
EXPOSE 3306 6379 8080
#EXPOSE 80/tcp
#EXPOSE 80/udp

#ADD [--chown=<user>:<group>] <src>... <dest>
#ADD [--chown=<user>:<group>] ["<src>",... "<dest>"](此表格包含所需的路径 空格)
#ADD指令复制新文件、目录或远程文件的url<src>并将它们添加到图像的文件系统路径
ADD test relativeDir/
ADD test /absoluteDir/

# 将当前主机目录内容拷贝至镜像文件夹  ADD可以下载压缩文件并自动解压，一般情况下用COPY
COPY .. /code

#指令集的工作目录RUN, CMD, ENTRYPOINT, COPY和ADD跟随它的指令Dockerfile。
#如果WORKDIR不存在,将创建它,即使它不用于任何 后续Dockerfile
#可多次指定，当容器启动后最后一个dir为容器当前工作目录
WORKDIR /path/to/workdir

#ENV <key> <value>
#ENV <key>=<value> ...
#设置镜像环境变量，可在docker run -env 中改变相关值
ENV WEB_PORT=9969

#ENTRYPOINT ["executable", "param1", "param2"] (执行形式,优先)
#ENTRYPOINT command param1 param2
#docker run -it xxx -a  与cmd的却别在于，ENTRYPOINT会拼接命令（实际为传入的执行参数），cmd则是覆盖 ls -l -a
#注意点
#1.一个dockerfile至少有一个ENTRYPOINT或CMD
#2.可执行容器应该用ENTRYPOINT
#3.CMD会被传入的命令参数覆盖掉
#4.都在容器启动时运行，ENTRYPOINT指令，往往用于设置容器启动后的第一个命令，这对一个容器来说往往是固定的。
#CMD指令，往往用于设置容器启动的第一个命令的默认参数，这对一个容器来说可以是变化的。
ENTRYPOINT["ls","-l"]
CMD["ls","-l"]
#挂载文件路径
VOLUME ["/data"]
# 作用于子镜像，基于现有镜像构筑新镜像时会执行，类型于继承,指令可能不会触发FROM或MAINTAINER指令
ONBUILD ADD .. /app/src
ONBUILD RUN /usr/local/bin/python-build --dir /app/src

#==================================================
FORM python:3.6
COPY .. /code
WORKDIR /code
RUN pip install -r requirements.txt