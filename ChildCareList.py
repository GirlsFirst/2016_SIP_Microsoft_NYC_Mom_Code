import random
mom_code_tip0 = ["Figuring out what your baby is upset about is major guessing game(no pun intended).",
 "After having to guess if they are hunger,messy, or just want some attention another factor could be that your baby is gassy.",
 "When coming out of the womb babies are born with the Moro, or startle,reflex.",
 "If your baby's private parts are a bit bigger than usual it might be due to swelling caused by pressure exerted on your baby during birth.",
 "If your baby seems hungry all the time it’s due to your baby’s growing appetite.",
 "Babies who are breastfed tend to be more hungry than babies who are not.",
 "Breast milk is more quickly digested and more completely absorbed than formula.",
 "Skin-to-skin contact with your baby allows you and your baby to build a stronger bond.",
 "When making eye contact with your baby it will allow your baby to recognize your face and starts to build their memory.",
 "While many may think honey would be a good thing to feed to your newborn it is actually contains a bacteria that can germinate in a baby’s developing digestive system."]

length = len(mom_code_tip0)
random_number = random.randint(0, length -1)
print (mom_code_tip0 [random_number])

