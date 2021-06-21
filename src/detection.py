def get_exclamation_coefficient(text):
    # In average, with training data set, (2 times more ! for fake than non fake news) but only 1 in 3 articles (fake news) had !
    amount = text.count("!")   
    return (amount/2, 0.3*amount**2+0.9)

def get_total_length_coefficient(text):
    total_length = len(text) / 500
    fake = max(-13659040 + (2154.389 -  -13659040)/(1+(total_length/73864090000)**(0.3929395)),0)/2000
    non_fake = max(-8*(total_length-11)**2+800,0)/2000
    return (non_fake, fake) 

def get_global_coefficient(text):
    fake_coeff = 0
    non_fake_coeff = 0

    # Coefficient by exclamation point
    exclam_coeff = get_exclamation_coefficient(sentence)
    non_fake_coeff += exclam_coeff[0]
    fake_coeff += exclam_coeff[1]

    # Coefficient by total text length
    total_length_coeff = get_total_length_coefficient(sentence)
    non_fake_coeff += total_length_coeff[0]
    fake_coeff += total_length_coeff[1]

    # Output
    return (non_fake_coeff,fake_coeff)
    

if __name__ == "__main__":
    sentence = "Hello World!"
    print(get_global_coefficient(sentence))
    
    