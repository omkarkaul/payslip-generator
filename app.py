## driver script for payslip generator
# hashtag lesh get dis bread :)
from payslip_model import Payslip

payslip = Payslip()

payslip.write_text(20,20, "git init PAY ME 3 HUNNIT THOUSAND")

payslip.output("payslip.pdf")