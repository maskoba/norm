import QtQuick 2.11
import QtQuick.Window 2.11
import QtQuick.Controls 2.4
import QtQuick.Controls.Material 2.0

Window {
    visible: true
    width: 800
    height: 480
    Material.theme: Material.Dark

    View1Form {
        id: view1Form
        button4.onClicked: {
            Qt.quit()
        }
        button5.onClicked:{
            backend.start_worker5()
        }
        button.onClicked:{
            if(button.checked){
                backend.start_worker0(true)
            }
            else{
                backend.start_worker0(false)
            }
        }
        button1.onClicked:{
            if(button1.checked){
                backend.start_worker1(true)
            }
            else{
                backend.start_worker1(false)
            }
        }
        button2.onClicked:{
            if(button2.checked){
                backend.start_worker2(true)
            }
            else{
                backend.start_worker2(false)
            }
        }
        button3.onClicked:{
            if(button3.checked){
                backend.start_worker3(true)
            }
            else{
                backend.start_worker3(false)
            }
            backend.on_timer()
        }
        anchors.fill: parent
    }
    function inputLevel(level) {
        switch (level / 2) {
            case 0:
                if (level % 2)
                    view1Form.label.color = "#00FF00"
                else
                    view1Form.label.color = "#00000000"
                break;
        
            case 1:
                if (level % 2)
                    view1Form.label1.color = "#00FF00"
                else
                    view1Form.label1.color = "#00000000"
                break;
        
            case 2:
                if (level % 2)
                    view1Form.label2.color = "#00FF00"
                else
                    view1Form.label2.color = "#00000000"
                break;
        
            case 3:
                if (level % 2)
                    view1Form.label3.color = "#00FF00"
                else
                    view1Form.label3.color = "#00000000"
                break;
        
            case 4:
                if (level % 2)
                    view1Form.label4.color = "#00FF00"
                else
                    view1Form.label4.color = "#00000000"
                break;
        
            case 5:
                if (level % 2)
                    view1Form.label5.color = "#00FF00"
                else
                    view1Form.label5.color = "#00000000"
                break;
        
            default:
                break;
        }
        view1Form.label.color = "#00FF00"
        console.log("> ValueChangeing from_python = " + level);
    }
}


