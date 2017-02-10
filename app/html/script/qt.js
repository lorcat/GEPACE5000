/*
author: Konstantin Glazyrin
email: konstantin.glazyrin@desy.de

Should come after jsquery and plugins
Main proxy object/purpose for communications with qt application
*/

function ExternalCommunicationQt(){
    // main class taking care for external communications
}

ExternalCommunicationQt.prototype.parseNewData = function(data){
    // moves Qt splitter to the left part
    console.debug("ExtCom. : parsing new data ("+data+")");

    if(data!=null && data!=undefined){
        if(data.length != undefined && data.length>0){
            var timestamp = data[0]['timestamp'.toUpperCase()];
            nick = "Timestamp";
            $("."+nick+" .header").text(nick);
            $("."+nick+" .data").text(timestamp);
            $("."+nick).attr('title', 'timestamp');

            data.forEach(function(obj,i){
                nick = obj['attr'.toUpperCase()];
                data = obj['datastr'.toUpperCase()];
                desc = obj['desc'.toUpperCase()];
                console.debug(data);

                if(data==undefined || data==null){
                    data = new String(obj["DATA"]);
                }

                $("."+nick+" .header").text(nick);
                $("."+nick+" .data").text(data);
                $("."+nick).attr('title', desc);
            });
        }
    }
}

// class for managing external communications with Qt
var ExtQt = new ExternalCommunicationQt();