function calculateCoolingLoad() {
    var area = parseFloat(document.getElementById("area").value);
    var occupants = parseInt(document.getElementById("occupants").value);
    var buildingType = document.getElementById("buildingType").value;
    var outdoorTemp = parseFloat(document.getElementById("outdoorTemp").value);
    var indoorTemp = parseFloat(document.getElementById("indoorTemp").value);
    var u = 30;  // Overall heat transfer coefficient in W/m²°C
    
    var coolingLoad;
    if (buildingType === "residential") {
        coolingLoad = 100 * occupants;
    } else if (buildingType === "commercial") {
        coolingLoad = 150 * occupants;
    } else {
        document.getElementById("result").innerHTML = "Invalid building type";
        return;
    }
    
    var qConduction = u * area * (outdoorTemp - indoorTemp);
    var sensibleCoolingLoad = qConduction + coolingLoad;
    
    var resultHTML = "Sensible Cooling Load: " + sensibleCoolingLoad + " W";
    document.getElementById("result").innerHTML = resultHTML;
}
