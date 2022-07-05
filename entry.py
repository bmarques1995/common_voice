import pandas as pd

#lendo csv
dataset = pd.read_csv("treino.csv")

print(dataset)

#selecionando partes do csv
data = dataset.iloc[7:15, 1:2].values


indexName = ['id','y']

#inserção de dados
out_data = []

out_data.append([3500, 'sixties'])
out_data.append([3501, 'fourties'])
out_data.append([3502, 'teens'])
out_data.append([3503, 'twinties'])

#gravando para csv
output = pd.DataFrame(out_data, columns=indexName)

output.to_csv("sampler_state.csv", encoding='utf-8', index=False)

print(output)

print(data)