def percentage(part, whole):
    return 100 * float(part) / float(whole)


def df_to_latex(path, df):
    with open(path, 'w') as f:
        f.write(df.to_latex(index=False))
