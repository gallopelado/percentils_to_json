import json

def convert_to_json(data_text):
    data = []
    for line in open(data_text, "r"):
        if line != 'Month\tL\tM\tS\tSD\tP01\tP1\tP3\tP5\tP10\tP15\tP25\tP50\tP75\tP85\tP90\tP95\tP97\tP99\tP999\n':
            month, l, m, s, sd, *percentiles = line.split()
            percentiles = [float(percentile) for percentile in percentiles]
            data.append({
                "Month": int(month),
                "L": float(l),
                "M": float(m),
                "S": float(s),
                "SD": float(sd),
                "P01": float(percentiles[0]),
                "P1": float(percentiles[1]),
                "P3": float(percentiles[2]),
                "P5": float(percentiles[3]),
                "P10": float(percentiles[4]),
                "P15": float(percentiles[5]),
                "P25": float(percentiles[6]),
                "P50": float(percentiles[7]),
                "P75": float(percentiles[8]),
                "P85": float(percentiles[9]),
                "P90": float(percentiles[10]),
                "P95": float(percentiles[11]),
                "P97": float(percentiles[12]),
                "P99": float(percentiles[13]),
                "P999": float(percentiles[14]) if len(percentiles)-1 == 14 else None
                })
    return data

def convert_to_json_without_sd(data_text):
    data = []
    for line in open(data_text, "r"):
        if line != 'Month\tL\tM\tS\tP01\tP1\tP3\tP5\tP10\tP15\tP25\tP50\tP75\tP85\tP90\tP95\tP97\tP99\tP999\n':
            month, l, m, s, *percentiles = line.split()
            percentiles = [float(percentile) for percentile in percentiles]
            data.append({
                "Month": int(month),
                "L": float(l),
                "M": float(m),
                "S": float(s),
                "P01": float(percentiles[0]),
                "P1": float(percentiles[1]),
                "P3": float(percentiles[2]),
                "P5": float(percentiles[3]),
                "P10": float(percentiles[4]),
                "P15": float(percentiles[5]),
                "P25": float(percentiles[6]),
                "P50": float(percentiles[7]),
                "P75": float(percentiles[8]),
                "P85": float(percentiles[9]),
                "P90": float(percentiles[10]),
                "P95": float(percentiles[11]),
                "P97": float(percentiles[12]),
                "P99": float(percentiles[13]),
                "P999": float(percentiles[14])
                })
    return data

def write_json(data, output_file):
    with open(output_file, "w") as f:
        json.dump(data, f)

def join_all():
    perimetro_cefalico_m_23 = convert_to_json("./txt/tab_hcfa_boys_p_0_5.txt")

    perimetro_cefalico_f_23 = convert_to_json("./txt/tab_hcfa_girls_p_0_5.txt")

    peso_m_23 = convert_to_json_without_sd("./txt/tab_wfa_boys_p_0_5.txt")

    peso_f_23 = convert_to_json_without_sd("./txt/tab_wfa_girls_p_0_5.txt")

    talla_m_23 = convert_to_json("./txt/tab_lhfa_boys_p_0_2.txt")
    talla_m_23.pop()
    talla_m_24 = convert_to_json("./txt/tab_lhfa_boys_p_2_5.txt")

    talla_f_23 = convert_to_json("./txt/tab_lhfa_girls_p_0_2.txt")
    talla_f_23.pop()
    talla_f_24 = convert_to_json("./txt/tab_lhfa_girls_p_2_5.txt")

    imc_m_23 = convert_to_json_without_sd("./txt/tab_bmi_boys_p_0_2.txt")
    imc_m_23.pop()
    imc_m_24 = convert_to_json_without_sd("./txt/tab_bmi_boys_p_2_5.txt")

    imc_f_23 = convert_to_json_without_sd("./txt/tab_bmi_girls_p_0_2.txt")
    imc_f_23.pop()
    imc_f_24 = convert_to_json_without_sd("./txt/tab_bmi_girls_p_2_5.txt")

    total = {
        'perimetroCefalico': {
            'masculino': perimetro_cefalico_m_23,
            'femenino': perimetro_cefalico_f_23
        },
        'peso': {
            'masculino': peso_m_23,
            'femenino': peso_f_23
        },
        'talla': {
            'masculino': talla_m_23 + talla_m_24,
            'femenino': talla_f_23 + talla_f_24
        },
        'imc': {
            'masculino': imc_m_23 + imc_m_24,
            'femenino': imc_f_23 + imc_f_24
        }
    }
    return total

write_json(join_all(), "final.json")