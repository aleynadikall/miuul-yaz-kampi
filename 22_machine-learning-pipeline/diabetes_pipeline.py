################################################
# End-to-End Diabetes Machine Learning Pipeline II
################################################

import joblib
import pandas as pd
from lightgbm import LGBMClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, VotingClassifier, AdaBoostClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_validate, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from xgboost import XGBClassifier


################################################
# Helper Functions
################################################

# utils.py
# helpers.py

# Data Preprocessing & Feature Engineering
def grab_col_names(dataframe, cat_th=10, car_th=20):
    """

    Veri setindeki kategorik, numerik ve kategorik fakat kardinal değişkenlerin isimlerini verir.
    Not: Kategorik değişkenlerin içerisine numerik görünümlü kategorik değişkenler de dahildir.

    Parameters
    ------
        dataframe: dataframe
                Değişken isimleri alınmak istenilen dataframe
        cat_th: int, optional
                numerik fakat kategorik olan değişkenler için sınıf eşik değeri
        car_th: int, optinal
                kategorik fakat kardinal değişkenler için sınıf eşik değeri

    Returns
    ------
        cat_cols: list
                Kategorik değişken listesi
        num_cols: list
                Numerik değişken listesi
        cat_but_car: list
                Kategorik görünümlü kardinal değişken listesi

    Examples
    ------
        import seaborn as sns
        df = sns.load_dataset("iris")
        print(grab_col_names(df))


    Notes
    ------
        cat_cols + num_cols + cat_but_car = toplam değişken sayısı
        num_but_cat cat_cols'un içerisinde.
        Return olan 3 liste toplamı toplam değişken sayısına eşittir: cat_cols + num_cols + cat_but_car = değişken sayısı

    """

    # cat_cols, cat_but_car
    cat_cols = [col for col in dataframe.columns if dataframe[col].dtypes == "O"]
    num_but_cat = [col for col in dataframe.columns if dataframe[col].nunique() < cat_th and
                   dataframe[col].dtypes != "O"]
    cat_but_car = [col for col in dataframe.columns if dataframe[col].nunique() > car_th and
                   dataframe[col].dtypes == "O"]
    cat_cols = cat_cols + num_but_cat
    cat_cols = [col for col in cat_cols if col not in cat_but_car]

    # num_cols
    num_cols = [col for col in dataframe.columns if dataframe[col].dtypes != "O"]
    num_cols = [col for col in num_cols if col not in num_but_cat]

    # print(f"Observations: {dataframe.shape[0]}")
    # print(f"Variables: {dataframe.shape[1]}")
    # print(f'cat_cols: {len(cat_cols)}')
    # print(f'num_cols: {len(num_cols)}')
    # print(f'cat_but_car: {len(cat_but_car)}')
    # print(f'num_but_cat: {len(num_but_cat)}')
    return cat_cols, num_cols, cat_but_car


def outlier_thresholds(dataframe, col_name, q1=0.25, q3=0.75):
    quartile1 = dataframe[col_name].quantile(q1)
    quartile3 = dataframe[col_name].quantile(q3)
    interquantile_range = quartile3 - quartile1
    up_limit = quartile3 + 1.5 * interquantile_range
    low_limit = quartile1 - 1.5 * interquantile_range
    return low_limit, up_limit


def replace_with_thresholds(dataframe, variable):
    low_limit, up_limit = outlier_thresholds(dataframe, variable)
    dataframe.loc[(dataframe[variable] < low_limit), variable] = low_limit
    dataframe.loc[(dataframe[variable] > up_limit), variable] = up_limit


def one_hot_encoder(dataframe, categorical_cols, drop_first=False):
    dataframe = pd.get_dummies(dataframe, columns=categorical_cols, drop_first=drop_first)
    return dataframe


def diabetes_data_prep(dataframe):
    dataframe.columns = [col.upper() for col in dataframe.columns]

    # Glucose
    dataframe['NEW_GLUCOSE_CAT'] = pd.cut(x=dataframe['GLUCOSE'], bins=[-1, 139, 200], labels=["normal", "prediabetes"])

    # Age
    dataframe.loc[(dataframe['AGE'] < 35), "NEW_AGE_CAT"] = 'young'
    dataframe.loc[(dataframe['AGE'] >= 35) & (dataframe['AGE'] <= 55), "NEW_AGE_CAT"] = 'middleage'
    dataframe.loc[(dataframe['AGE'] > 55), "NEW_AGE_CAT"] = 'old'

    # BMI
    dataframe['NEW_BMI_RANGE'] = pd.cut(x=dataframe['BMI'], bins=[-1, 18.5, 24.9, 29.9, 100],
                                        labels=["underweight", "healty", "overweight", "obese"])

    # BloodPressure
    dataframe['NEW_BLOODPRESSURE'] = pd.cut(x=dataframe['BLOODPRESSURE'], bins=[-1, 79, 89, 123],
                                            labels=["normal", "hs1", "hs2"])

    cat_cols, num_cols, cat_but_car = grab_col_names(dataframe, cat_th=5, car_th=20)

    cat_cols = [col for col in cat_cols if "OUTCOME" not in col]

    df = one_hot_encoder(dataframe, cat_cols, drop_first=True)

    cat_cols, num_cols, cat_but_car = grab_col_names(df, cat_th=5, car_th=20)

    replace_with_thresholds(df, "INSULIN")

    X_scaled = StandardScaler().fit_transform(df[num_cols])
    df[num_cols] = pd.DataFrame(X_scaled, columns=df[num_cols].columns)

    y = df["OUTCOME"]
    X = df.drop(["OUTCOME"], axis=1)

    return X, y


# Base Models
def base_models(X, y, scoring="roc_auc"):
    print("Base Models....")
    classifiers = [('LR', LogisticRegression()),
                   ('KNN', KNeighborsClassifier()),
                   ("SVC", SVC()),
                   ("CART", DecisionTreeClassifier()),
                   ("RF", RandomForestClassifier()),
                   ('Adaboost', AdaBoostClassifier()),
                   ('GBM', GradientBoostingClassifier()),
                   ('XGBoost', XGBClassifier(use_label_encoder=False, eval_metric='logloss')),
                   ('LightGBM', LGBMClassifier()),
                   # ('CatBoost', CatBoostClassifier(verbose=False))
                   ]

    for name, classifier in classifiers:
        cv_results = cross_validate(classifier, X, y, cv=3, scoring=scoring)
        print(f"{scoring}: {round(cv_results['test_score'].mean(), 4)} ({name}) ")


# Hyperparameter Optimization

# config.py

knn_params = {"n_neighbors": range(2, 50)}

cart_params = {'max_depth': range(1, 20),
               "min_samples_split": range(2, 30)}

rf_params = {"max_depth": [8, 15, None],
             "max_features": [5, 7, "auto"],
             "min_samples_split": [15, 20],
             "n_estimators": [200, 300]}

xgboost_params = {"learning_rate": [0.1, 0.01],
                  "max_depth": [5, 8],
                  "n_estimators": [100, 200],
                  "colsample_bytree": [0.5, 1]}

lightgbm_params = {"learning_rate": [0.01, 0.1],
                   "n_estimators": [300, 500],
                   "colsample_bytree": [0.7, 1]}

classifiers = [('KNN', KNeighborsClassifier(), knn_params),
               ("CART", DecisionTreeClassifier(), cart_params),
               ("RF", RandomForestClassifier(), rf_params),
               ('XGBoost', XGBClassifier(use_label_encoder=False, eval_metric='logloss'), xgboost_params),
               ('LightGBM', LGBMClassifier(), lightgbm_params)]


def hyperparameter_optimization(X, y, cv=3, scoring="roc_auc"):
    print("Hyperparameter Optimization....")
    best_models = {}
    for name, classifier, params in classifiers:
        print(f"########## {name} ##########")
        cv_results = cross_validate(classifier, X, y, cv=cv, scoring=scoring)
        print(f"{scoring} (Before): {round(cv_results['test_score'].mean(), 4)}")

        gs_best = GridSearchCV(classifier, params, cv=cv, n_jobs=-1, verbose=False).fit(X, y)
        final_model = classifier.set_params(**gs_best.best_params_)

        cv_results = cross_validate(final_model, X, y, cv=cv, scoring=scoring)
        print(f"{scoring} (After): {round(cv_results['test_score'].mean(), 4)}")
        print(f"{name} best params: {gs_best.best_params_}", end="\n\n")
        best_models[name] = final_model
    return best_models


# Stacking & Ensemble Learning
def voting_classifier(best_models, X, y):
    print("Voting Classifier...")
    voting_clf = VotingClassifier(estimators=[('KNN', best_models["KNN"]), ('RF', best_models["RF"]),
                                              ('LightGBM', best_models["LightGBM"])],
                                  voting='soft').fit(X, y)
    cv_results = cross_validate(voting_clf, X, y, cv=3, scoring=["accuracy", "f1", "roc_auc"])
    print(f"Accuracy: {cv_results['test_accuracy'].mean()}")
    print(f"F1Score: {cv_results['test_f1'].mean()}")
    print(f"ROC_AUC: {cv_results['test_roc_auc'].mean()}")
    return voting_clf


################################################
# Pipeline Main Function
################################################

def main():
    df = pd.read_csv("datasets/diabetes.csv")
    X, y = diabetes_data_prep(df)
    base_models(X, y)
    best_models = hyperparameter_optimization(X, y)
    voting_clf = voting_classifier(best_models, X, y)
    joblib.dump(voting_clf, "voting_clf.pkl")
    return voting_clf


# Sol yandaki play'e basarak bir çalıştıralım.
# Şu anda buradaki ana çalışma scriptimiz diabetes_pipeline dosyası oldu.

if __name__ == "__main__":
    print("İşlem başladı")
    main()

# Bunu komut satırından önce python'ı çağırarak ondan sonra bu scripti çağırarak gerçekleştirmek istiyoruz.
# Proje bölümüne geldik. Bu dosyamız her neredeyse o dosyanın olduğu dizine gelmeliyiz. Eğer programı en başlarından
# beri hoca ile takip ediyorsak şu anda çalışma dizinimizin içerisinde olmamız gerekir. Dosyada sağa tık yapıp Open In
# Terminal diyoruz. Bu terminal şu anda bizim içerisinde çalıştığımız çalışma dizinidir. Dosyamızın bu çalışma dizininin
# içinde olması lazım. Bu çalışma dizininin altındaysa python diabetes_pipeline.py dediğimizde çalışması gerekir.
# diabetes_pipeline.py hangi dosya altındaysa onda terminali açıyoruz.

# Şu anda terminal/komut satırından işletim sistemi seviyesinde bir makine öğrenmesi projesini çalıştırdık. Bu işin en
# core en temel noktasıdır. Burada hazırlamış olduğumuz bu pipeline bunun dışında kalan işlerin en önemli kısmı ve
# kalbidir. Dolayısıyla profesyonel yaşantımızda bir proje kapsamındaburaya eklenmesi gereken diğer bazı şeyler de
# olacaktır. Ama temel odak ve pekiişmesi gereken nokta burasıdır.

# Peki hangi bileşenler lazım gibi bir soru olabilir. Ne tür işlemlerle karşılaşabiliriz gibi bir soru olabilir. Daha
# öncesinde bir kısmından bahsetmiştik. Şimdi bunları biraz ele alalım.

# 1
# git github entegrasyonuyla bu iş gitmelidir. Burada veri bilimş ve makine öğrenmesi işleri için git etkileşimlerinin
# normal bir yazılım geliştirme sürecine göre daha düşük olabileceğini söyleyebiliriz ve riskin biraz daha düşük
# olduğunu, kullanım frekansının biraz daha düşük olduğunu söyleyebiliriz. Bu kullanıp kullanmamakla ilgili değil
# kullanma esnasındaki kullanım frekansını ifade ediyoruz.

# 2
# makefile gibi otomasyon tooları tercih edilebilir. Bu makefile'ın python versiyonu da vardır. Daha kolaylaştırılmış
# bir versiyonudur. Nedir makefile? Biz bu projeye bir komut satırı arayüzü yazmadık. Yani işletim sistemi seviyesinden
# komutlar vererek bu içerideki scripti biçimlendirebilecek işlemler yapmadık. Buna benzer işlemleri git igthub
# işlemlerini veya çeşitli görevleri makefile kod otomasyon aracıyla yapabiliriz. Mesela örnek olması için terminalde
# make git dediğimizde sadece örneğin bir git add commit ve push işlemlerini peş peşe yaptırabiliriz. Makefile bir kod
# otomasyonu, linux aracıdır. Burada örneğin make git kısayoluna git add git commit ve git push gibi 3 4 tane işlemi
# ekleyip bu şekilde bir kısayolla işlemleri otomatize edebiliriz. Ya da örnek olması için bir makefile içrisinde make
# train diye bir şey oluştururuz, bu make train'in içerisinde az önce yapmış olduğumuz  python diabetes_pipeline.py kodu
# olur. Bunu make train şeklinde daha kısa bir şekilde ifade ederek bu işlemi çalıştırabiliriz. Yani özetle ifade etmek
# gerekirse bu komut satırında uzun olabilecek bazı kod yazımlarını daha pratik daha kısa bir şekilde peş peşe de
# çeşitli kodları çalıştırabilecek şekilde yapabileceğimiz bir yapıdır makefile.

# 3
# veri tabanlarından veri okunuyor olacak. Veri tabanından veri okumak da oldukça kolaydır. Bağlantı bilgileri
# neticesinde bağlantıyı gerçekleştirip daha sonra tekrar o tabloları geriye basacak şekilde kullanımlar
# değerlendiriliyor olunur.

# 4
# log : Süreçlerin logunu tutmak olabilir.

# 5
# class : Fonksiyonları class yapılarına çevirmek olabilir.

# 6
# docker : Benim bilgisayarım da çalışıyordu, sunucuda çalışmıyor ifadesinden hatırlayabiliriz. Ortak bir işletme
# process'i, ortak bir işletme prosedürü çerçevesinde dockerize edilmiş projeler docker barındıran tüm ortamlarda ilk
# oluşturdukları ortamdaki gibi çalışabilmektedir. Dolayısıyla buradaki dependency management problemlerini,
# gereklilikleri ve benzeri noktaları daha iyi proje kapsamında taşıyabilmek için bir docker işlemine sokulabilir.

# 7
# requirement.txt 
