import QtQuick 2.11
import QtQuick.Controls 2.4

ApplicationWindow {
    visible: true
    width: 800
    height: 480

    View1Form {
        id: view1Form
        button4.onClicked: {
            Qt.quit()
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
        }
        anchors.fill: parent
    }

    function inputLevel(level) {
        switch (level) {
            case 0:
                view1Form.label.color = "#dd000000";
                break;
        
            case 1:
                view1Form.label.color = "#00FF00";
                break;
        
            case 2:
                view1Form.label1.color = "#dd000000";
                break;
        
            case 3:
                view1Form.label1.color = "#00FF00";
                break;
        
            case 4:
                view1Form.label2.color = "#dd000000";
                break;
        
            case 5:
                view1Form.label2.color = "#00FF00";
                break;
        
            case 6:
                view1Form.label3.color = "#dd000000";
                break;
        
            case 7:
                view1Form.label3.color = "#00FF00";
                break;
        
            case 8:
                view1Form.label4.color = "#dd000000";
                break;
        
            case 9:
                view1Form.label4.color = "#00FF00";
                break;
        
            case 10:
                view1Form.label5.color = "#dd000000";
                break;
        
            case 11:
                view1Form.label5.color = "#00FF00";
                break;
        
            default:
                break;
        }
        console.log("> ValueChangeing from_python = " + level);
    }
}


