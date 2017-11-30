def interpret_corr_result(corr, p_val, confidence=0.95, print_res=False):
    if p_val < 1.0 - confidence:
        if corr < 0:
            relationship = 'negative'
        else:
            relationship = 'positive'
        if abs(corr) > 0.25:
            strength = 'moderate'
        elif abs(corr) > 0.75:
            strength = 'large'
        else:
            strength = 'none or small'
        print(
            'Computed correlation {} which can be interpreted as {} {} linear dependence is statistically significant on confidence interval [{},1].'.format(
                str(corr), strength, relationship, str(confidence)))
    else:
        print(
            'Due to p-value {} the computed correlation is not statistically significant on confidence interval [{},1], we could not confirm any linear dependence.'.format(
                str(p_val), str(confidence)))
