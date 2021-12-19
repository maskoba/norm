// import QtQuick 2.4
// import QtQuick.Controls 2.3
import QtQuick.Layouts 1.0
import QtQuick 2.11
import QtQuick.Controls 2.4
import QtQuick.Controls.Material 2.0

Item {
    id: element
    Material.theme: Material.Dark
    property alias button: button
    property alias label: label
    property alias label5: label5
    property alias label4: label4
    property alias label3: label3
    property alias label2: label2
    property alias label1: label1
    property alias button3: button3
    property alias button2: button2
    property alias button1: button1
    property alias button4: button4
    property alias button5: button5

    RowLayout {
        y: 127
        anchors.right: parent.right
        anchors.rightMargin: 140
        anchors.left: parent.left
        anchors.leftMargin: 140

        Rectangle {
            id: rectangle
            color: "#00000000"
            property int property0: 0
            border.color: "#000000"
            Layout.preferredHeight: 40
            Layout.preferredWidth: 80

            Label {
                id: label
                text: "IN0"
                anchors.fill: parent
                verticalAlignment: Text.AlignVCenter
                horizontalAlignment: Text.AlignHCenter
            }
        }

        Rectangle {
            id: rectangle1
            color: "#00000000"
            border.color: "#000000"
            Layout.preferredHeight: 40
            Layout.preferredWidth: 80

            Label {
                id: label1
                text: qsTr("IN1")
                verticalAlignment: Text.AlignVCenter
                horizontalAlignment: Text.AlignHCenter
                anchors.fill: parent
            }
        }

        Rectangle {
            id: rectangle2
            color: "#00000000"
            border.color: "#000000"
            Layout.preferredHeight: 40
            Layout.preferredWidth: 80

            Label {
                id: label2
                text: qsTr("IN2")
                verticalAlignment: Text.AlignVCenter
                horizontalAlignment: Text.AlignHCenter
                anchors.fill: parent
            }
        }

        Rectangle {
            id: rectangle3
            color: "#00000000"
            border.color: "#000000"
            Layout.preferredHeight: 40
            Layout.preferredWidth: 80

            Label {
                id: label3
                text: qsTr("IN3")
                verticalAlignment: Text.AlignVCenter
                horizontalAlignment: Text.AlignHCenter
                anchors.fill: parent
            }
        }

        Rectangle {
            id: rectangle4
            color: "#00000000"
            border.color: "#000000"
            Layout.preferredHeight: 40
            Layout.preferredWidth: 80

            Label {
                id: label4
                text: qsTr("IN4")
                verticalAlignment: Text.AlignVCenter
                horizontalAlignment: Text.AlignHCenter
                anchors.fill: parent
            }
        }

        Rectangle {
            id: rectangle5
            color: "#00000000"
            border.color: "#000000"
            Layout.preferredHeight: 40
            Layout.preferredWidth: 80

            Label {
                id: label5
                text: qsTr("IN5")
                verticalAlignment: Text.AlignVCenter
                horizontalAlignment: Text.AlignHCenter
                anchors.fill: parent
            }
        }
    }

    RowLayout {
        y: 210
        height: 48
        anchors.right: parent.right
        anchors.rightMargin: 65
        anchors.left: parent.left
        anchors.leftMargin: 140

        Button {
            id: button
            text: qsTr("OUT0")
            checkable: true
        }

        Button {
            id: button1
            text: qsTr("OUT1")
            checkable: true
        }

        Button {
            id: button2
            text: qsTr("OUT2")
            checkable: true
        }

        Button {
            id: button3
            text: qsTr("OUT3")
            checkable: true
        }
    }

    Label {
        id: label6
        y: 8
        height: 78
        text: qsTr("Raspberry Pi  I /O TEST")
        font.pointSize: 32
        verticalAlignment: Text.AlignVCenter
        horizontalAlignment: Text.AlignHCenter
        anchors.right: parent.right
        anchors.left: parent.left
    }

    Button {
        id: button4
        y: 288
        text: qsTr("QUIT")
        anchors.right: parent.right
        anchors.rightMargin: 200
        anchors.left: parent.left
        anchors.leftMargin: 200
    }

    Button {
        id: button5
        x: 200
        y: 373
        text: qsTr("Button")
    }
}




/*##^## Designer {
    D{i:0;autoSize:true;height:480;width:800}D{i:3;anchors_height:64;anchors_width:132;anchors_x:19;anchors_y:"-236"}
D{i:5;anchors_height:64;anchors_width:132;anchors_x:"-59";anchors_y:"-227"}D{i:7;anchors_height:64;anchors_width:132;anchors_x:"-147";anchors_y:"-227"}
D{i:9;anchors_height:64;anchors_width:132;anchors_x:"-241";anchors_y:"-238"}D{i:11;anchors_height:64;anchors_width:132;anchors_x:"-314";anchors_y:"-233"}
D{i:13;anchors_height:64;anchors_width:132;anchors_x:558;anchors_y:329}D{i:1;anchors_x:140}
}
 ##^##*/
