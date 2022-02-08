import os
import sys
from PySide2.QtWidgets import QApplication
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtCore import QObject, Signal, Property, QUrl, Slot
import pigpio
from datetime import datetime

count = 0
preset = 3

gpio_IN0 = 4    # GPIO4(7)
gpio_IN1 = 17   # GPIO17(11)
gpio_IN2 = 27   # GPIO27(13)
gpio_IN3 = 22   # GPIO22(15)
gpio_IN4 = 10   # GPIO10(19)
gpio_IN5 = 9    # GPIO9(21)

gpio_OUT0 = 14  # GPIO14(8)
gpio_OUT1 = 15  # GPIO15(10)
gpio_OUT2 = 23  # GPIO23(16)
gpio_OUT3 = 24  # GPIO24(18)

class Backend(QObject):
    progress_changed = Signal(int)

    def __init__(self):
        QObject.__init__(self)

    @Slot(bool)
    def start_worker0(self,on):
        if on:
            pi.write(gpio_OUT0, 1)
        else:
            pi.write(gpio_OUT0, 0)

    @Slot(bool)
    def start_worker1(self,on):
        if on:
            pi.write(gpio_OUT1, 1)
        else:
            pi.write(gpio_OUT1, 0)

    @Slot(bool)
    def start_worker2(self,on):
        if on:
            pi.write(gpio_OUT2, 1)
        else:
            pi.write(gpio_OUT2, 0)

    @Slot(bool)
    def start_worker3(self,on):
        if on:
            pi.write(gpio_OUT3, 1)
        else:
            pi.write(gpio_OUT3, 0)

    @Slot(int)
    def set_level(self,num):
        self.progress_changed.emit(num)

def main():
    global backend
    """ 環境変数に Qt Quick Controls 2 のコンフィグファイル設定 を追加する
      環境変数 QT_QUICK_CONTROLS_CONF に対して、本 Code と同じ
      ディレクトリにある qtquickcontrols2.conf
      ( Qt Quick Controls 2 の Configuration File ファイル)
      を設定
    """
    os.environ["QT_QUICK_CONTROLS_CONF"] = "qtquickcontrols2.conf"

    app = QApplication([])

    engine = QQmlApplicationEngine()
    # QML経由でアクセスするカウントダウン処理 Backendクラス
    #   のインスタンスを生成する
    backend = Backend()
    # backend クラスを QML の backend としてバインディングする
    engine.rootContext().setContextProperty("backend", backend)

    url = QUrl("main.qml")
    # QML ファイルのロード
    engine.load(url)
    # ルートオブジェクトのリストが見つからない場合は
    # 起動できないため、終了する
    if not engine.rootObjects():
        sys.exit(-1)

    # 先頭の root オブジェクト (Main.qml 内の root オブジェクト ) を取得
    root = engine.rootObjects()[0]
    # Main.qml 内の function inputlevel() と接続
    backend.progress_changed.connect(root.inputLevel)

    if pi.read(gpio_IN0):       # 初期設定
        backend.set_level(0)
    else:
        backend.set_level(1)
    if pi.read(gpio_IN1):
        backend.set_level(2)
    else:
        backend.set_level(3)
    if pi.read(gpio_IN2):
        backend.set_level(4)
    else:
        backend.set_level(5)
    if pi.read(gpio_IN3):
        backend.set_level(6)
    else:
        backend.set_level(7)
    if pi.read(gpio_IN4):
        backend.set_level(8)
    else:
        backend.set_level(9)
    if pi.read(gpio_IN5):
        backend.set_level(10)
    else:
        backend.set_level(11)

    pi.callback(gpio_IN0, pigpio.EITHER_EDGE, interrupt)   # 割り込み処理用の関数
    pi.callback(gpio_IN1, pigpio.EITHER_EDGE, interrupt)   # 割り込み処理用の関数
    pi.callback(gpio_IN2, pigpio.EITHER_EDGE, interrupt)   # 割り込み処理用の関数
    pi.callback(gpio_IN3, pigpio.EITHER_EDGE, interrupt)   # 割り込み処理用の関数
    pi.callback(gpio_IN4, pigpio.EITHER_EDGE, interrupt)   # 割り込み処理用の関数
    pi.callback(gpio_IN5, pigpio.EITHER_EDGE, interrupt)   # 割り込み処理用の関数

    ret = app.exec_()

    pi.write(gpio_OUT0, 0)
    pi.write(gpio_OUT1, 0)
    pi.write(gpio_OUT2, 0)
    pi.write(gpio_OUT3, 0)

    sys.exit(ret)

def interrupt(GPIO, level, tick):
    global backend
    if GPIO == gpio_IN0:
        if pi.read(gpio_IN0):
            backend.set_level(0)
        else:
            backend.set_level(1)
    elif GPIO == gpio_IN1:
        if pi.read(gpio_IN1):
            backend.set_level(2)
        else:
            backend.set_level(3)
    elif GPIO == gpio_IN2:
        if pi.read(gpio_IN2):
            backend.set_level(4)
        else:
            backend.set_level(5)
    elif GPIO == gpio_IN3:
        if pi.read(gpio_IN3):
            backend.set_level(6)
        else:
            backend.set_level(7)
    elif GPIO == gpio_IN4:
        if pi.read(gpio_IN4):
            backend.set_level(8)
        else:
            backend.set_level(9)
    elif GPIO == gpio_IN5:
        if pi.read(gpio_IN5):
            backend.set_level(10)
        else:
            backend.set_level(11)

pi = pigpio.pi()   # GPIOにアクセスするためのインスタンスを作成
pi.set_mode(gpio_IN0, pigpio.INPUT)   # GPIO pin を入力設定
pi.set_mode(gpio_IN1, pigpio.INPUT)   # GPIO pin を入力設定
pi.set_mode(gpio_IN2, pigpio.INPUT)   # GPIO pin を入力設定
pi.set_mode(gpio_IN3, pigpio.INPUT)   # GPIO pin を入力設定
pi.set_mode(gpio_IN4, pigpio.INPUT)   # GPIO pin を入力設定
pi.set_mode(gpio_IN5, pigpio.INPUT)   # GPIO pin を入力設定
# pi.set_pull_up_down(gpio_IN0, pigpio.PUD_DOWN) # GPIO入力をプルダウンする
# pi.set_pull_up_down(gpio_IN1, pigpio.PUD_DOWN)
# pi.set_pull_up_down(gpio_IN2, pigpio.PUD_DOWN)
# pi.set_pull_up_down(gpio_IN3, pigpio.PUD_DOWN)
# pi.set_pull_up_down(gpio_IN4, pigpio.PUD_DOWN)
# pi.set_pull_up_down(gpio_IN5, pigpio.PUD_DOWN)
pi.set_pull_up_down(gpio_IN0, pigpio.PUD_UP) # GPIO入力をプルアップする
pi.set_pull_up_down(gpio_IN1, pigpio.PUD_UP)
pi.set_pull_up_down(gpio_IN2, pigpio.PUD_UP)
pi.set_pull_up_down(gpio_IN3, pigpio.PUD_UP)
pi.set_pull_up_down(gpio_IN4, pigpio.PUD_UP)
pi.set_pull_up_down(gpio_IN5, pigpio.PUD_UP)
pi.set_mode(gpio_OUT0, pigpio.OUTPUT)   # GPIO pin を出力設定
pi.set_mode(gpio_OUT1, pigpio.OUTPUT)   # GPIO pin を出力設定
pi.set_mode(gpio_OUT2, pigpio.OUTPUT)   # GPIO pin を出力設定
pi.set_mode(gpio_OUT3, pigpio.OUTPUT)   # GPIO pin を出力設定
pi.write(gpio_OUT0, 0)
pi.write(gpio_OUT1, 0)
pi.write(gpio_OUT2, 0)
pi.write(gpio_OUT3, 0)
pi.set_glitch_filter(gpio_IN0,10000)
pi.set_glitch_filter(gpio_IN1,10000)
pi.set_glitch_filter(gpio_IN2,10000)
pi.set_glitch_filter(gpio_IN3,10000)
pi.set_glitch_filter(gpio_IN4,10000)
pi.set_glitch_filter(gpio_IN5,10000)
pi.set_noise_filter(gpio_IN0, 1000, 500)
pi.set_noise_filter(gpio_IN1, 1000, 500)
pi.set_noise_filter(gpio_IN2, 1000, 500)
pi.set_noise_filter(gpio_IN3, 1000, 500)
pi.set_noise_filter(gpio_IN4, 1000, 500)
pi.set_noise_filter(gpio_IN5, 1000, 500)

if __name__ == '__main__':
    main()
