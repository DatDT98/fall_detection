FROM ubuntu:18.04
# ...
RUN apt-get update && apt-get install -y \
        software-properties-common
    RUN add-apt-repository ppa:deadsnakes/ppa
    RUN apt-get update && apt-get install -y \
        python3.7 \
        python3-pip
    RUN apt-get update && apt-get install -y \
        python3-distutils \
        python3-setuptools
    RUN python3.7 -m pip install pip --upgrade pip
RUN apt install libgl1-mesa-glx -y
RUN apt install git -y

# update pip
RUN python3.7 -m pip install wheel
RUN pip3 install openpifpaf
EXPOSE 50054

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt



COPY . /fall_detection_service
WORKDIR /fall_detection_service
#COPY ./fall_detection_service/venv/lib/python3.7/site-packages /venv/lib/python3.7/site-packages
