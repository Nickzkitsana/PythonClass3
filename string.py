#tuple
score = (10.5,13,14,24,41.5,50)
scoreSort = sorted(score,reverse=True)
print('{0}'.format(type(score)))
print('Range : {0}'.format(len(score)))
print('Max : {0}'.format(max(score)))
print('Min : {0}'.format(min(score)))
print('Summery : {0}'.format(sum(score)))
print('{0}'.format(score[0]))
print('{0}'.format(scoreSort))
print('-'*30)
for i in range(len(score)):
    print('{}'.format(score[i]))
print('-'*30)
for i in score: #for-each
    print('{}'.format(i))

