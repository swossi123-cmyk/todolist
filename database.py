from sqlalchemy import create_engine # اتصال معل قاعدة البيانات
from sqlalchemy.orm import sessionmaker, declarative_base # declarative_base → لإنشاء الكلاس الأساسي الذي سترث منه جميع الجداول.  , sessionmaker = جلسة تتعامل بها مع قاعدة البيانات


DB_URL = "sqlite:///./todolist.db" # انشى قاعدة ببانات اسمها todolist.db

engine = create_engine(DB_URL, #عنوان قاعدة البيانات
                       connect_args={"check_same_thread":False}) # اسمح لعدة Requests باستعمال SQLite

SessionLocal = sessionmaker(bind=engine,# اربط Session بقاعدة البيانات
                             autoflush=False,# لا ترسل البيانات تلقائياً
                               autocommit=False)# لا تحفظ البيانات تلقائياً، انتظر db.commit()

Base = declarative_base() #  جميع الجداول عليها الوراث من bASE