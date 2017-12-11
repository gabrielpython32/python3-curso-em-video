n = int(input('Digite a medida em metros: '))
km = n / 1000
hm = n / 100
dam = n / 10
dm = n * 10
cm = n * 100
mm = n * 1000
print('A medida de {}m corresponde a:\n{}km\n{}hm\n{}dam\n{}dm\n{}cm\n{}mm'.format(n, km, hm, dam, dm, cm, mm))
