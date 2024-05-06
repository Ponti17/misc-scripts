import argparse
import numpy as np

parser = argparse.ArgumentParser(description="Gain Converter")
parser.add_argument("-r", "--ratio", action="store_true", help="voltage/power gain as ratio (default of no option)")
parser.add_argument("-d", "--db", action="store_true", help="voltage/power gain in dB")
parser.add_argument("-p", "--power", action="store_true", help="power gain")
parser.add_argument("-c", "--cmrr", action="store_true", help="common mode rejection ratio")
parser.add_argument("gain")
args = parser.parse_args()

if not any([args.ratio, args.db, args.cmrr]):
    args.ratio = True

# Voltage gain = 20 * log10(Vout/Vin)
# Power gain = 10 * log10(Pout/Pin)
prod = 20
if args.power:
    prod = 10

if args.ratio:
    gain = float(args.gain)
    print(f"Gain ratio: {gain}")
    print(f"Gain in dB: {np.round(prod * np.log10(gain),2)}")

elif args.db:
    gain = float(args.gain)
    print(f"Gain in dB: {gain}")
    print(f"Gain ratio: {np.round(10 ** (gain / prod), 2):,}")
    
elif args.cmrr:
    gain = float(args.gain)
    print(f"CMRR: {gain}")
    print(f"CM Gain: Adm / {np.round(10 ** (gain / 20),2)}")
