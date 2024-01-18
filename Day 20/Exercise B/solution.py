import functions as fc

br, fl, cc, ut, qu = fc.get_data("code.txt")

total, ps, st, tt, tl, th = fc.press_button(br, fl, cc, ut, qu)

print(total)