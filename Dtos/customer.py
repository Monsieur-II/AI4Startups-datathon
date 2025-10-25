from pydantic import BaseModel


class Customer(BaseModel):
    customerId: str
    emailAddress: str
    frequency: str
    monetary: str
    avgOrderValue: str
    customerLifetimeDays: str
    purchaseRate: str
    customerType: str
    attribution: str
    totalItemsSold: str
