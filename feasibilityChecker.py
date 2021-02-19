import time
import requests
import json

class feasibilityChecker():

    def retrieveManufaqConstrains(self):
            URL = "http://127.0.0.1:3030/chair/update"

            selectQuery = 'PREFIX kbe:<http://kbe.com/chair_design.owl#> '+\
                        'SELECT ?backHeightMax ?backHeightMin ?chairColor ?chairMaterial ?legLengthMax ?legLengthMin ?legSideMax ?legSideMin ?seatSideMax ?seatSideMin ?backShape ?shapeMaterial'+\
                        'WHERE'+\
                        '{'+\
                        '?back a kbe:Back.'+\
                        '?back kbe:hasBackHeightMax ?backHeightMax.'+\
                        '?back kbe:hasBackHeightMin ?backHeightMin.'+\
                        '?chair a kbe:Chair.'+\
                        '?chair kbe:hasColor ?chairColor.'+\
                        '?chair kbe:hasMaterial ?chairMaterial.'+\
                        '?leg a kbe:Leg.'+\
                        '?leg kbe:hasLegLengthMax ?legLengthMax.'+\
                        '?leg kbe:hasLegLengthMin ?legLengthMin.'+\
                        '?leg kbe:hasLegSideMax ?legSideMax.'+\
                        '?leg kbe:hasLegSideMin ?legSideMin.'+\
                        '?shape a kbe:Shape.'+\
                        '?shape kbe:hasMaterial ?shapeMaterial.'+\
                        '?shape kbe:hasShape ?backShape.'+\
                        '?seat a kbe:Seat.'+\
                        '?seat kbe:hasSeatSideMax ?seatSideMax.'+\
                        '?seat kbe:hasSeatSideMin ?seatSideMin.'+\
                        '}'

            PARAMS = {'query':selectQuery}

            r = requests.get(url = URL, params = PARAMS)
            print("r: ",r)
            data = r.json()

            #arrangement of data_pool [backHeightMax,backHeightMin,chairColor,chairMaterial
            # legLengthMax,legLengthMin,legSideMax,legSideMin,shapeMaterial,backShape
            # seatSideMax,seatSideMin]
            data_pool = [data['results']['bindings'][0]['backHeightMax']['value'],\
                        data['results']['bindings'][0]['backHeightMin']['value'],\
                        data['results']['bindings'][0]['chairColor']['value'],\
                        data['results']['bindings'][0]['chairMaterial']['value'],\
                        data['results']['bindings'][0]['legLengthMax']['value'],\
                        data['results']['bindings'][0]['legLengthMin']['value'],\
                        data['results']['bindings'][0]['legSideMax']['value'],\
                        data['results']['bindings'][0]['legSideMin']['value'],\
                        data['results']['bindings'][0]['shapeMaterial']['value'],\
                        data['results']['bindings'][0]['backShape']['value'],\
                        data['results']['bindings'][0]['seatSideMax']['value'],\
                        data['results']['bindings'][0]['seatSideMin']['value']]
            
            return data_pool

    def retrieveCustomerData(self):
        #MUST BE MODIFIED FOR CUSTOMER DATA
        URL = "http://127.0.0.1:3030/chair/update"

            selectQuery = 'PREFIX kbe:<http://kbe.com/chair_design.owl#> '+\
                        'SELECT ?backHeight ?chairColor ?chairMaterial ?legLength ?legSide ?seatSide ?backShape ?shapeMaterial'+\
                        'WHERE'+\
                        '{'+\
                        '?back a kbe:Back.'+\
                        '?back kbe:hasBackHeight ?backHeight.'+\
                        '?chair a kbe:Chair.'+\
                        '?chair kbe:hasColor ?chairColor.'+\
                        '?chair kbe:hasMaterial ?chairMaterial.'+\
                        '?leg a kbe:Leg.'+\
                        '?leg kbe:hasLegLength ?legLength.'+\
                        '?leg kbe:hasLegSide ?legSide.'+\
                        '?shape a kbe:Shape.'+\
                        '?shape kbe:hasMaterial ?shapeMaterial.'+\
                        '?shape kbe:hasShape ?backShape.'+\
                        '?seat a kbe:Seat.'+\
                        '?seat kbe:hasSeatSide ?seatSide.'+\
                        '}'

            PARAMS = {'query':selectQuery}

            r = requests.get(url = URL, params = PARAMS)
            print("r: ",r)
            data = r.json()

            data_pool = [data['results']['bindings'][0]['backHeightMax']['value'],\
                        data['results']['bindings'][0]['backHeightMin']['value'],\
                        data['results']['bindings'][0]['chairColor']['value'],\
                        data['results']['bindings'][0]['chairMaterial']['value'],\
                        data['results']['bindings'][0]['legLengthMax']['value'],\
                        data['results']['bindings'][0]['legLengthMin']['value'],\
                        data['results']['bindings'][0]['legSideMax']['value'],\
                        data['results']['bindings'][0]['legSideMin']['value'],\
                        data['results']['bindings'][0]['shapeMaterial']['value'],\
                        data['results']['bindings'][0]['backShape']['value'],\
                        data['results']['bindings'][0]['seatSideMax']['value'],\
                        data['results']['bindings'][0]['seatSideMin']['value']]
            
            return data_pool

    def feasibilityCheck(self):
        """
        # we agree that this should be in the dfaServer.py?
        #for-loop with list for expandability and KBE-friendly
        production_intz_param = [leg_length1, leg_side1, seat_side1, back_height1, chair_color, back_shape_material1, chair_material1, number_chair1]
        flagOK = False
        if(production_intz_param[0] > leg_lengthLow) and (production_intz_param[0] < leg_lengthUp):
            if (production_intz_param[1] > leg_sideLow) and (production_intz_param[1] < leg_sideUp):
                if (production_intz_param[2] > seat_sideLow) and (production_intz_param[2] < leg_sideUp):
                    if (production_intz_param[3] > back_heightLow) and (production_intz_param[3]< back_heightUp):
                        if production_intz_param[4] in chair_color:
                            if production_intz_param[5] in back_shape_material:
                                if production_intz_param[6] in chair_material:
                                    if materialCalculation(production_intz_param[7]):
                                        s.wfile.write(bytes('OK','utf-8'))
                                        print("The parameters are accepted")
                                        flagOK = True
        else:
            s.wfile.write(bytes('Not OK', 'utf-8'))
            print("The parameters given is not accepted")
        """
