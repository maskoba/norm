import os
import sys
from PySide2.QtWidgets import QApplication
from PySide2.QtQml import QQmlApplicationEngine
# from PySide2.QtCore import QObject, Slot, Signal, QTimer, QUrl, QThread
from PySide2.QtCore import QObject, Signal, Property, QUrl, Slot, QThread, QTimer, Qt
from PySide2.QtQml import qmlRegisterType
import pigpio
import queue
import threading
import time
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

class ThreadPress(threading.Thread):
    """Threaded Press"""
    def __init__(self, queue):
        threading.Thread.__init__(self,name='Press')
        self.queue = queue
        self.state = 0
        self.preset = 8
        self.total = 0
        self.hako = 0
        self.backend = Backend()

    def run(self):
        while True:
            try:
                #grabs host from queue
                host = self.queue.get(True,1)
                if self.state == 0:             # IDLE
                    self.hako += 1
                    self.total += 1
                    if self.hako == self.preset:
                        # pi.write(gpio_OUT1, 1)
                        self.state = 1
                elif self.state == 1:           # リセット待ち
                    if host == 8:
                        self.hako = 0
                        self.state = 0
                self.backend.value_changed.emit()
                print("state: %s total: %s hako: %s" % (self.state,self.total,self.hako))
                # if (host % 2) == 1:
                #     print("%s at ON time: %s" % (self.getName(), datetime.now()))
                # else:
                #     print("%s at OFF time: %s" % (self.getName(), datetime.now()))
                #signals to queue job is done
                self.queue.task_done()
            except:
                now = datetime.now()
                print("%s at time: %s" % (self.getName(), now))


class Backend(QObject):
    value_changed = Signal()
    progress_changed = Signal(str)

    def __init__(self):
        QObject.__init__(self)
        self.value_changed.connect(self.on_timer)

    @Slot(bool)
    def start_worker0(self,on):
        if on:
            queue1.put(1)
        else:
            queue1.put(0)

    @Slot(bool)
    def start_worker1(self,on):
        if on:
            queue1.put(3)
        else:
            queue1.put(2)

    @Slot(bool)
    def start_worker2(self,on):
        if on:
            queue1.put(5)
        else:
            queue1.put(4)

    @Slot(bool)
    def start_worker3(self,on):
        if on:
            queue1.put(7)
        else:
            queue1.put(6)

    @Slot()
    def start_worker5(self):
        queue1.put(8)

    @Property(int,notify=progress_changed)
    def count(self):
        return 1

    @count.setter
    def set_count(self,num):
        self.progress_changed.emit(num)
    
    @Slot()
    def on_timer(self):
        self.set_count("1")

def main():
    # global pytext
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
    # backend.value_changed.connect(backend.on_timer)

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

    ret = app.exec_()

    pi.write(gpio_OUT0, 0)
    pi.write(gpio_OUT1, 0)
    pi.write(gpio_OUT2, 0)
    pi.write(gpio_OUT3, 0)

    sys.exit(ret)

def counter_incr():
    global count
    if ( count == preset):
        return
    count += 1
    # self.lb3["text"] = '{:04}'.format(count)
    if ( count == preset):
        pi.write(gpio_OUT1, 1)


def interrupt(GPIO, level, tick):
    counter_incr()
    # app.counter_incr()

pi = pigpio.pi()   # GPIOにアクセスするためのインスタンスを作成
pi.set_mode(gpio_IN0, pigpio.INPUT)   # GPIO pin を入力設定
pi.set_mode(gpio_IN1, pigpio.INPUT)   # GPIO pin を入力設定
pi.set_mode(gpio_IN2, pigpio.INPUT)   # GPIO pin を入力設定
pi.set_mode(gpio_IN3, pigpio.INPUT)   # GPIO pin を入力設定
pi.set_mode(gpio_IN4, pigpio.INPUT)   # GPIO pin を入力設定
pi.set_mode(gpio_IN5, pigpio.INPUT)   # GPIO pin を入力設定
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
pi.callback(gpio_IN0, pigpio.FALLING_EDGE, interrupt)   # 割り込み処理用の関数
pi.callback(gpio_IN1, pigpio.FALLING_EDGE, interrupt)   # 割り込み処理用の関数
pi.callback(gpio_IN2, pigpio.FALLING_EDGE, interrupt)   # 割り込み処理用の関数
pi.callback(gpio_IN3, pigpio.FALLING_EDGE, interrupt)   # 割り込み処理用の関数
pi.callback(gpio_IN4, pigpio.FALLING_EDGE, interrupt)   # 割り込み処理用の関数
pi.callback(gpio_IN5, pigpio.FALLING_EDGE, interrupt)   # 割り込み処理用の関数

queue1 = queue.Queue()          # プレス制御
pres = ThreadPress(queue1)
pres.setDaemon(True)
pres.start()

if __name__ == '__main__':
    main()
