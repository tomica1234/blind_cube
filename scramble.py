import random, copy
import streamlit as st

st.title('目隠しキューバーへの道')
def U(ecubes, ccubes):
    box = [ecubes[0][:], ccubes[0][:]]
    elist = [0, 4, 3, 8]
    clist = [0, 3, 7, 4]
    for i in range(3):
        ecubes[elist[i]] = ecubes[elist[i+1]]

        ccubes[clist[i]][0] = ccubes[clist[i+1]][0]
        ccubes[clist[i]][1] = ccubes[clist[i+1]][2]
        ccubes[clist[i]][2] = ccubes[clist[i+1]][1]

    ecubes[elist[-1]] = box[0]

    ccubes[clist[-1]][0] = box[1][0]
    ccubes[clist[-1]][1] = box[1][2]
    ccubes[clist[-1]][2] = box[1][1]

    return ecubes, ccubes

def U_reverse(ecubes, ccubes):
    box = [ecubes[0][:], ccubes[0][:]]
    elist = [0, 8, 3, 4]
    clist = [0, 4, 7, 3]
    for i in range(3):
        ecubes[elist[i]] = ecubes[elist[i+1]]

        ccubes[clist[i]][0] = ccubes[clist[i+1]][0]
        ccubes[clist[i]][1] = ccubes[clist[i+1]][2]
        ccubes[clist[i]][2] = ccubes[clist[i+1]][1]

    ecubes[elist[-1]] = box[0]

    ccubes[clist[-1]][0] = box[1][0]
    ccubes[clist[-1]][1] = box[1][2]
    ccubes[clist[-1]][2] = box[1][1]
    
    return ecubes, ccubes

def U2(ecubes, ccubes):
    box = [ecubes[0][:], ecubes[8][:], ccubes[0][:], ccubes[4][:]]
    elist = [0, 8, 3, 4]
    clist = [0, 4, 7, 3]
    for i in range(2):
        ecubes[elist[i]] = ecubes[elist[i+2]]

        ccubes[clist[i]] = ccubes[clist[i+2]]

    ecubes[elist[-2]] = box[0]
    ecubes[elist[-1]] = box[1]

    ccubes[clist[-2]] = box[2]
    ccubes[clist[-1]] = box[3]
    
    return ecubes, ccubes

def F(ecubes, ccubes):
    box = [ecubes[3][:], ccubes[3][:]]
    elist = [3, 7, 2, 11]
    clist = [3, 2, 6, 7]
    for i in range(3):
        ecubes[elist[i]][0] = ecubes[elist[i+1]][1]
        ecubes[elist[i]][1] = ecubes[elist[i+1]][0]

        ccubes[clist[i]][0] = ccubes[clist[i+1]][2]
        ccubes[clist[i]][1] = ccubes[clist[i+1]][1]
        ccubes[clist[i]][2] = ccubes[clist[i+1]][0]

    ecubes[elist[-1]][0] = box[0][1]
    ecubes[elist[-1]][1] = box[0][0]

    ccubes[clist[-1]][0] = box[1][2]
    ccubes[clist[-1]][1] = box[1][1]
    ccubes[clist[-1]][2] = box[1][0]

    return ecubes, ccubes

def F_reverse(ecubes, ccubes):
    box = [ecubes[3][:], ccubes[3][:]]
    elist = [3, 11, 2, 7]
    clist = [3, 7, 6, 2]
    for i in range(3):
        ecubes[elist[i]][0] = ecubes[elist[i+1]][1]
        ecubes[elist[i]][1] = ecubes[elist[i+1]][0]

        ccubes[clist[i]][0] = ccubes[clist[i+1]][2]
        ccubes[clist[i]][1] = ccubes[clist[i+1]][1]
        ccubes[clist[i]][2] = ccubes[clist[i+1]][0]

    ecubes[elist[-1]][0] = box[0][1]
    ecubes[elist[-1]][1] = box[0][0]

    ccubes[clist[-1]][0] = box[1][2]
    ccubes[clist[-1]][1] = box[1][1]
    ccubes[clist[-1]][2] = box[1][0]

    return ecubes, ccubes

def F2(ecubes, ccubes):
    box = [ecubes[3][:], ecubes[11][:], ccubes[3][:], ccubes[7][:]]
    elist = [3, 11, 2, 7]
    clist = [3, 7, 6, 2]
    for i in range(2):
        ecubes[elist[i]] = ecubes[elist[i+2]]

        ccubes[clist[i]] = ccubes[clist[i+2]]

    ecubes[elist[-2]] = box[0]
    ecubes[elist[-1]] = box[1]
    
    ccubes[clist[-2]] = box[2]
    ccubes[clist[-1]] = box[3]
    
    return ecubes, ccubes

def R(ecubes, ccubes):
    box = [ecubes[8][:], ccubes[4][:]]
    elist = [8, 11, 10, 9]
    clist = [4, 7, 6, 5]
    for i in range(3):
        ecubes[elist[i]] = ecubes[elist[i+1]]

        ccubes[clist[i]][0] = ccubes[clist[i+1]][1]
        ccubes[clist[i]][1] = ccubes[clist[i+1]][0]
        ccubes[clist[i]][2] = ccubes[clist[i+1]][2]

    ecubes[elist[-1]] = box[0]

    ccubes[clist[-1]][0] = box[1][1]
    ccubes[clist[-1]][1] = box[1][0]
    ccubes[clist[-1]][2] = box[1][2]

    return ecubes, ccubes

def R_reverse(ecubes, ccubes):
    box = [ecubes[8][:], ccubes[4][:]]
    elist = [8, 9, 10, 11]
    clist = [4, 5, 6, 7]
    for i in range(3):
        ecubes[elist[i]] = ecubes[elist[i+1]]

        ccubes[clist[i]][0] = ccubes[clist[i+1]][1]
        ccubes[clist[i]][1] = ccubes[clist[i+1]][0]
        ccubes[clist[i]][2] = ccubes[clist[i+1]][2]

    ecubes[elist[-1]] = box[0]

    ccubes[clist[-1]][0] = box[1][1]
    ccubes[clist[-1]][1] = box[1][0]
    ccubes[clist[-1]][2] = box[1][2]
    
    return ecubes, ccubes

def R2(ecubes, ccubes):
    box = [ecubes[8][:], ecubes[9][:], ccubes[4][:], ccubes[5][:]]
    elist = [8, 9, 10, 11]
    clist = [4, 5, 6, 7]
    for i in range(2):
        ecubes[elist[i]] = ecubes[elist[i+2]]

        ccubes[clist[i]] = ccubes[clist[i+2]]

    ecubes[elist[-2]] = box[0]
    ecubes[elist[-1]] = box[1]
    
    ccubes[clist[-2]] = box[2]
    ccubes[clist[-1]] = box[3]
    
    return ecubes, ccubes

def D(ecubes, ccubes):
    box = [ecubes[2][:], ccubes[2][:]]
    elist = [2, 6, 1, 10]
    clist = [2, 1, 5, 6]
    for i in range(3):
        ecubes[elist[i]] = ecubes[elist[i+1]]

        ccubes[clist[i]][0] = ccubes[clist[i+1]][0]
        ccubes[clist[i]][1] = ccubes[clist[i+1]][2]
        ccubes[clist[i]][2] = ccubes[clist[i+1]][1]

    ecubes[elist[-1]] = box[0]

    ccubes[clist[-1]][0] = box[1][0]
    ccubes[clist[-1]][1] = box[1][2]
    ccubes[clist[-1]][2] = box[1][1]

    return ecubes, ccubes

def D_reverse(ecubes, ccubes):
    box = [ecubes[2][:], ccubes[2][:]]
    elist = [2, 10, 1, 6]
    clist = [2, 6, 5, 1]
    for i in range(3):
        ecubes[elist[i]] = ecubes[elist[i+1]]

        ccubes[clist[i]][0] = ccubes[clist[i+1]][0]
        ccubes[clist[i]][1] = ccubes[clist[i+1]][2]
        ccubes[clist[i]][2] = ccubes[clist[i+1]][1]

    ecubes[elist[-1]] = box[0]

    ccubes[clist[-1]][0] = box[1][0]
    ccubes[clist[-1]][1] = box[1][2]
    ccubes[clist[-1]][2] = box[1][1]

    return ecubes, ccubes

def D2(ecubes, ccubes):
    box = [ecubes[2][:], ecubes[10][:], ccubes[2][:], ccubes[6][:]]
    elist = [2, 10, 1, 6]
    clist = [2, 6, 5, 1]
    for i in range(2):
        ecubes[elist[i]] = ecubes[elist[i+2]]

        ccubes[clist[i]] = ccubes[clist[i+2]]

    ecubes[elist[-2]] = box[0]
    ecubes[elist[-1]] = box[1]

    ccubes[clist[-2]] = box[2]
    ccubes[clist[-1]] = box[3]
    
    return ecubes, ccubes

def B(ecubes, ccubes):
    box = [ecubes[0][:], ccubes[0][:]]
    elist = [0, 9, 1, 5]
    clist = [0, 4, 5, 1]
    for i in range(3):
        ecubes[elist[i]][0] = ecubes[elist[i+1]][1]
        ecubes[elist[i]][1] = ecubes[elist[i+1]][0]

        ccubes[clist[i]][0] = ccubes[clist[i+1]][2]
        ccubes[clist[i]][1] = ccubes[clist[i+1]][1]
        ccubes[clist[i]][2] = ccubes[clist[i+1]][0]

    ecubes[elist[-1]][0] = box[0][1]
    ecubes[elist[-1]][1] = box[0][0]

    ccubes[clist[-1]][0] = box[1][2]
    ccubes[clist[-1]][1] = box[1][1]
    ccubes[clist[-1]][2] = box[1][0]

    return ecubes, ccubes

def B_reverse(ecubes, ccubes):
    box = [ecubes[0][:], ccubes[0][:]]
    elist = [0, 5, 1, 9]
    clist = [0, 1, 5, 4]
    for i in range(3):
        ecubes[elist[i]][0] = ecubes[elist[i+1]][1]
        ecubes[elist[i]][1] = ecubes[elist[i+1]][0]

        ccubes[clist[i]][0] = ccubes[clist[i+1]][2]
        ccubes[clist[i]][1] = ccubes[clist[i+1]][1]
        ccubes[clist[i]][2] = ccubes[clist[i+1]][0]

    ecubes[elist[-1]][0] = box[0][1]
    ecubes[elist[-1]][1] = box[0][0]

    ccubes[clist[-1]][0] = box[1][2]
    ccubes[clist[-1]][1] = box[1][1]
    ccubes[clist[-1]][2] = box[1][0]

    return ecubes, ccubes

def B2(ecubes, ccubes):
    box = [ecubes[0][:], ecubes[5][:], ccubes[0][:], ccubes[1][:]]
    elist = [0, 5, 1, 9]
    clist = [0, 1, 5, 4]
    for i in range(2):
        ecubes[elist[i]] = ecubes[elist[i+2]]

        ccubes[clist[i]] = ccubes[clist[i+2]]

    ecubes[elist[-2]] = box[0]
    ecubes[elist[-1]] = box[1]

    ccubes[clist[-2]] = box[2]
    ccubes[clist[-1]] = box[3]
    
    return ecubes, ccubes

def L(ecubes, ccubes):
    box = [ecubes[4][:], ccubes[0][:]]
    elist = [4, 5, 6, 7]
    clist = [0, 1, 2, 3]
    for i in range(3):
        ecubes[elist[i]] = ecubes[elist[i+1]]

        ccubes[clist[i]][0] = ccubes[clist[i+1]][1]
        ccubes[clist[i]][1] = ccubes[clist[i+1]][0]
        ccubes[clist[i]][2] = ccubes[clist[i+1]][2]

    ecubes[elist[-1]] = box[0]

    ccubes[clist[-1]][0] = box[1][1]
    ccubes[clist[-1]][1] = box[1][0]
    ccubes[clist[-1]][2] = box[1][2]
    
    return ecubes, ccubes

def L_reverse(ecubes, ccubes):
    box = [ecubes[4][:], ccubes[0][:]]
    elist = [4, 7, 6, 5]
    clist = [0, 3, 2, 1]
    for i in range(3):
        ecubes[elist[i]] = ecubes[elist[i+1]]

        ccubes[clist[i]][0] = ccubes[clist[i+1]][1]
        ccubes[clist[i]][1] = ccubes[clist[i+1]][0]
        ccubes[clist[i]][2] = ccubes[clist[i+1]][2]

    ecubes[elist[-1]] = box[0]

    ccubes[clist[-1]][0] = box[1][1]
    ccubes[clist[-1]][1] = box[1][0]
    ccubes[clist[-1]][2] = box[1][2]

    return ecubes, ccubes

def L2(ecubes, ccubes):
    box = [ecubes[4][:], ecubes[7][:], ccubes[0][:], ccubes[3][:]]
    elist = [4, 7, 6, 5]
    clist = [0, 3, 2, 1]
    for i in range(2):
        ecubes[elist[i]] = ecubes[elist[i+2]]

        ccubes[clist[i]] = ccubes[clist[i+2]]

    ecubes[elist[-2]] = box[0]
    ecubes[elist[-1]] = box[1]

    ccubes[clist[-2]] = box[2]
    ccubes[clist[-1]] = box[3]
    
    return ecubes, ccubes

eindex_dict1 = {
    'あ': 0, 'い': 1, 'う': 2, 'え': 3,
    'た': 0, 'ち': 1, 'つ': 2, 'て': 3, 
    'か': 4, 'き': 5, 'く': 6, 'け': 7, 
    'な': 4, 'に': 5, 'ぬ': 6, 'ね': 7, 
    'さ': 8, 'し': 9, 'す': 10, 'せ': 11,
    'ら': 8, 'り': 9, 'る': 10, 'れ': 11,
}

eindex_dict2 = {
    'あ': 0, 'い': 0, 'う': 0, 'え': 0,
    'た': 1, 'ち': 1, 'つ': 1, 'て': 1, 
    'か': 0, 'き': 0, 'く': 0, 'け': 0, 
    'な': 1, 'に': 1, 'ぬ': 1, 'ね': 1, 
    'さ': 0, 'し': 0, 'す': 0, 'せ': 0,
    'ら': 1, 'り': 1, 'る': 1, 'れ': 1,
}

cindex_dict1 = {
    'あ': 0, 'い': 1, 'う': 2, 'え': 3,
    'た': 4, 'ち': 5, 'つ': 6, 'て': 7, 
    'か': 0, 'き': 1, 'く': 2, 'け': 3, 
    'な': 0, 'に': 1, 'ぬ': 2, 'ね': 3, 
    'さ': 4, 'し': 5, 'す': 6, 'せ': 7,
    'ら': 4, 'り': 5, 'る': 6, 'れ': 7,
}

cindex_dict2 = {
    'あ': 0, 'い': 0, 'う': 0, 'え': 0,
    'た': 0, 'ち': 0, 'つ': 0, 'て': 0, 
    'か': 1, 'き': 1, 'く': 1, 'け': 1, 
    'な': 2, 'に': 2, 'ぬ': 2, 'ね': 2, 
    'さ': 1, 'し': 1, 'す': 1, 'せ': 1,
    'ら': 2, 'り': 2, 'る': 2, 'れ': 2,
}

ecubes_sample = [
    ['あ', 'た'], ['い', 'ち'], ['う', 'つ'], ['え', 'て'],
    ['か', 'な'], ['き', 'に'], ['く', 'ぬ'], ['け', 'ね'],
    ['さ', 'ら'], ['し', 'り'], ['す', 'る'], ['せ', 'れ'],
]

ccubes_sample = [
    ['あ', 'か', 'な'], ['い', 'き', 'に'], ['う', 'く', 'ぬ'], ['え', 'け', 'ね'],
    ['た', 'さ', 'ら'], ['ち', 'し', 'り'], ['つ', 'す', 'る'], ['て', 'せ', 'れ'],
]

ecubes = [
    ['あ', 'た'], ['い', 'ち'], ['う', 'つ'], ['え', 'て'],
    ['か', 'な'], ['き', 'に'], ['く', 'ぬ'], ['け', 'ね'],
    ['さ', 'ら'], ['し', 'り'], ['す', 'る'], ['せ', 'れ'],
]

ccubes = [
    ['あ', 'か', 'な'], ['い', 'き', 'に'], ['う', 'く', 'ぬ'], ['え', 'け', 'ね'],
    ['た', 'さ', 'ら'], ['ち', 'し', 'り'], ['つ', 'す', 'る'], ['て', 'せ', 'れ'],
]

spincount = st.number_input('スクランブル回数',min_value=1,value=10)

if st.button('スクランブル'):
    spin1 = [random.randint(0, 5) for i in range(spincount)]
    spin2 = [random.randint(0, 2) for i in range(spincount)]
    for i in range(1, len(spin1)-1):
        lis = [j for j in range(6)]
        if spin1[i] == spin1[i+1]:
            if spin1[i-1] == spin1[i+1]:
                lis.remove(spin1[i-1])
            else:
                lis.remove(spin1[i-1])
                lis.remove(spin1[i+1])
            spin1[i] = random.choice(lis)

    spinmark = []

    for i in range(spincount):
        if spin1[i] == 0:
            if spin2[i] == 0:
                ecubes, ccubes = U(ecubes, ccubes)
                spinmark.append("U")
            elif spin2[i] == 1:
                ecubes, ccubes = U_reverse(ecubes, ccubes)
                spinmark.append("U'")
            elif spin2[i] == 2:
                ecubes, ccubes = U2(ecubes, ccubes)
                spinmark.append("U2")
            # print(ecubes)
        if spin1[i] == 1:
            if spin2[i] == 0:
                ecubes, ccubes = F(ecubes, ccubes)
                spinmark.append("F")
            elif spin2[i] == 1:
                ecubes, ccubes = F_reverse(ecubes, ccubes)
                spinmark.append("F'")
            elif spin2[i] == 2:
                ecubes, ccubes = F2(ecubes, ccubes)
                spinmark.append("F2")
            # print(ecubes)
        if spin1[i] == 2:
            if spin2[i] == 0:
                ecubes, ccubes = R(ecubes, ccubes)
                spinmark.append("R")
            elif spin2[i] == 1:
                ecubes, ccubes = R_reverse(ecubes, ccubes)
                spinmark.append("R'")
            elif spin2[i] == 2:
                ecubes, ccubes = R2(ecubes, ccubes)
                spinmark.append("R2")
            # print(ecubes)
        if spin1[i] == 3:
            if spin2[i] == 0:
                ecubes, ccubes = D(ecubes, ccubes)
                spinmark.append("D")
            elif spin2[i] == 1:
                ecubes, ccubes = D_reverse(ecubes, ccubes)
                spinmark.append("D'")
            elif spin2[i] == 2:
                ecubes, ccubes = D2(ecubes, ccubes)
                spinmark.append("D2")
            # print(ecubes)
        if spin1[i] == 4:
            if spin2[i] == 0:
                ecubes, ccubes = B(ecubes, ccubes)
                spinmark.append("B")
            elif spin2[i] == 1:
                ecubes, ccubes = B_reverse(ecubes, ccubes)
                spinmark.append("B'")
            elif spin2[i] == 2:
                ecubes, ccubes = B2(ecubes, ccubes)
                spinmark.append("B2")
            # print(ecubes)
        if spin1[i] == 5:
            if spin2[i] == 0:
                ecubes, ccubes = L(ecubes, ccubes)
                spinmark.append("L")
            elif spin2[i] == 1:
                ecubes, ccubes = L_reverse(ecubes, ccubes)
                spinmark.append("L'")
            elif spin2[i] == 2:
                ecubes, ccubes = L2(ecubes, ccubes)
                spinmark.append("L2")
            # print(ecubes)


    elist = []
    clist = []

    esolvelist = [8] + [i for i in range(12)]
    csolvelist = [i for i in range(8)]

    esolved = []
    csolved = []

    for i in esolvelist:
        if ecubes[i][0] in ecubes_sample[8]:
            continue
        if ecubes[i][0] != ecubes_sample[i][0]:
            data = ecubes_sample[i][0]
            if (data in esolved) == False:
                elist.append(data)
            while (data in esolved) == False:
                esolved.append(ecubes_sample[eindex_dict1[data]][0])
                esolved.append(ecubes_sample[eindex_dict1[data]][1])
                data = ecubes[eindex_dict1[data]][eindex_dict2[data]]
                elist.append(data)

    esolveway = [i for i in elist if i not in ecubes_sample[8]]

    if len(esolveway) % 2 == 1:
        box = ccubes[4][:]
        ccubes[4][0] = ccubes[7][0]
        ccubes[4][1] = ccubes[7][2]
        ccubes[4][2] = ccubes[7][1]

        ccubes[7][0] = box[0]
        ccubes[7][1] = box[2]
        ccubes[7][2] = box[1]

    for i in csolvelist:
        if ccubes[i][0] in ccubes_sample[0]:
            continue
        if ccubes[i][0] != ccubes_sample[i][0]:
            data = ccubes_sample[i][0]
            if (data in csolved) == False:
                clist.append(data)
            while (data in csolved) == False:
                csolved.append(ccubes_sample[cindex_dict1[data]][0])
                csolved.append(ccubes_sample[cindex_dict1[data]][1])
                csolved.append(ccubes_sample[cindex_dict1[data]][2])
                data = ccubes[cindex_dict1[data]][cindex_dict2[data]]
                clist.append(data)

    csolveway = [i for i in clist if i not in ccubes_sample[0]]

    st.write(' '.join(spinmark))
    st.write(''.join(esolveway))
    st.write(''.join(csolveway))