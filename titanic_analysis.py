import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('titanic.csv')


df['Age'] = df['Age'].fillna(df['Age'].median())

# Считаем выживаемость по полу
women = df[df['Sex'] == 'female']['Survived'].mean() * 100
men = df[df['Sex'] == 'male']['Survived'].mean() * 100
print(f"Выживаемость женщин: {women:.1f}%")
print(f"Выживаемость мужчин: {men:.1f}%")

# Считаем выживаемость по классу
class1 = df[df['Pclass'] == 1]['Survived'].mean() * 100
class2 = df[df['Pclass'] == 2]['Survived'].mean() * 100
class3 = df[df['Pclass'] == 3]['Survived'].mean() * 100
print(f"\n1 класс: {class1:.1f}%")
print(f"2 класс: {class2:.1f}%")
print(f"3 класс: {class3:.1f}%")

# Простая визуализация
plt.bar(['Женщины', 'Мужчины'], [women, men], color=['pink', 'blue'])
plt.title('Выживаемость по полу')
plt.ylabel('Процент')
plt.savefig('survival_by_sex.png')