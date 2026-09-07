import pandas as pd

df = pd.read_csv('ecommerce_data.csv')

# 1. إزالة أي بيانات مكررة أو مفقودة
df.drop_duplicates(inplace=True)
df.fillna(df.median(numeric_only=True), inplace=True)

# 2. حساب المبيعات الإجمالية وتقسيم العملاء (RFM Indicator)
df['TotalSpent'] = df['Sales'] * df['Quantity']

# تحديد العميل المتسرب (لم يشترِ منذ أكثر من 90 يوم)
df['Is_Churned'] = df['DaysSinceLastPurchase'].apply(lambda x: 1 if x > 90 else 0)

print(f"إجمالي المبيعات: ${df['TotalSpent'].sum():,.2f}")
print(f"نسبة العملاء المتسربين: {df['Is_Churned'].mean() * 100:.1f}%")