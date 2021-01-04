import json


class RestAPI:
    database = {}

    def __init__(self, database=None):
        self.database = database

    def get(self, url, payload=None):
        if url == '/users' and payload is None:
            return json.dumps(self.database)
        elif url == '/users' and payload:
            names = json.loads(payload)["users"]
            users = {"users": list(filter(lambda user: user["name"] in names,
                                          self.database["users"]))}
            return json.dumps(users)

    def post(self, url, payload=None):
        if url == "/add":
            new_user = {"name": json.loads(payload)["user"],
                        "owes": {}, "owed_by": {}, "balance": 0.0}
            self.database["users"].append(new_user)
            return json.dumps(new_user)
        elif url == "/iou":
            iou = json.loads(payload)
            lender = [i for i, _ in enumerate(self.database["users"]) if _['name'] == iou["lender"]][0]
            borrower = [i for i, _ in enumerate(self.database["users"]) if _['name'] == iou["borrower"]][0]

            amount = float(iou["amount"])
            self.database["users"][lender]["balance"] += amount
            self.database["users"][borrower]["balance"] -= amount

            #  Owes
            if (iou["borrower"] in self.database["users"][lender]["owes"].keys() and
                    iou["lender"] in self.database["users"][borrower]["owed_by"].keys()):
                if self.database["users"][lender]["owes"][iou["borrower"]] > amount:
                    self.database["users"][lender]["owes"][iou["borrower"]] -= amount
                    self.database["users"][borrower]["owed_by"][iou["lender"]] -= amount
                else:
                    balance = amount - self.database["users"][lender]["owes"][iou["borrower"]]
                    self.database["users"][lender]["owes"].pop(iou["borrower"])
                    self.database["users"][borrower]["owed_by"].pop(iou["lender"])
                    if balance > 0:
                        self.database["users"][lender]["owed_by"][iou["borrower"]] = balance
                        self.database["users"][borrower]["owes"][iou["lender"]] = balance

            #  Owed by
            elif (iou["borrower"] in self.database["users"][lender]["owed_by"].keys() and
                  iou["lender"] in self.database["users"][borrower]["owes"].keys()):
                self.database["users"][lender]["owed_by"][iou["borrower"]] += amount
                self.database["users"][borrower]["owes"][iou["lender"]] += amount

            #  No amount
            else:
                self.database["users"][lender]["owed_by"][iou["borrower"]] = amount
                self.database["users"][borrower]["owes"][iou["lender"]] = amount

            users = {"users": list(filter(lambda user: user["name"] in [iou["lender"], iou["borrower"]],
                                          self.database["users"]))}

            return json.dumps(users)
