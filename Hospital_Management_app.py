import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

class Hospital:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")

        # ------------------ Tk variables ------------------
        self.Nameoftablets = tk.StringVar()
        self.ref = tk.StringVar()
        self.Dose = tk.StringVar()
        self.NumberofTablets = tk.StringVar()
        self.Lot = tk.StringVar()
        self.Issuedate = tk.StringVar()
        self.ExpDate = tk.StringVar()
        self.DailyDose = tk.StringVar()
        self.SideEffect = tk.StringVar()
        self.FurtherInformation = tk.StringVar()
        self.StorageAdvice = tk.StringVar()
        self.DrivingUsingMachine = tk.StringVar() # This variable is not saved/fetched from DB, but kept for consistency
        self.HowToUseMedication = tk.StringVar() # This variable maps to DB column 'medication'
        self.PatientId = tk.StringVar()
        self.nhsNumber = tk.StringVar()
        self.PatientName = tk.StringVar()
        self.DateOfBirth = tk.StringVar()
        self.PatientAddress = tk.StringVar()
        self.BloodPressure = tk.StringVar() 

        # --- MySQL config: Ensure DB table 'data_full' exists with your 19 columns ---
        self.db_config = {
            "host": "localhost",
            "user": "root",
            "password": "yourpass",    # <-- UPDATE THIS with your MySQL password
            "database": "hospital_data"
        }

        # ------------------ Title ------------------
        lbltitle = tk.Label(
            self.root,
            bd=20,
            relief="ridge",
            text="+ HOSPITAL MANAGEMENT SYSTEM",
            fg="red",
            bg="white",
            font=("times new roman", 40, "bold")
        )
        lbltitle.pack(side="top", fill="x")

        # ==================== DataFrame ====================
        Dataframe = tk.Frame(self.root, bd=20, padx=20, relief="ridge")
        Dataframe.place(x=0, y=130, width=1530, height=400)

        DataframeLeft = tk.LabelFrame(
            Dataframe,
            bd=10,
            padx=20,
            relief="ridge",
            font=("arial", 12, "bold"),
            text="Patient Information"
        )
        DataframeLeft.place(x=0, y=5, width=980, height=350)

        DataframeRight = tk.LabelFrame(
            Dataframe,
            bd=10,
            padx=20,
            relief="ridge",
            font=("arial", 12, "bold"),
            text="Prescription"
        )
        DataframeRight.place(x=990, y=5, width=450, height=350)

        # ==================== ButtonFrame ====================
        Buttonframe = tk.Frame(self.root, bd=20, relief="ridge")
        Buttonframe.place(x=0, y=530, width=1530, height=70)

        # ==================== Details Frame ====================
        Detailsframe = tk.Frame(self.root, bd=20, relief="ridge")
        Detailsframe.place(x=0, y=600, width=1530, height=190)

        # ==================== DataFrameLeft widgets ====================
        
        # Row 0
        lblNameTablet = tk.Label(DataframeLeft, text="Names of Tablet", font=("arial", 12, "bold"), padx=2, pady=6)
        lblNameTablet.grid(row=0, column=0)
        comNametablet = ttk.Combobox(DataframeLeft, textvariable=self.Nameoftablets, state="readonly", font=("Myriad Pro", 12, "bold"), width=33)
        comNametablet["values"] = ("Nice", "Ibuprofen", "Pantoprazole", "Paracetamol", "Dolo 650", "Metformin", "Cetirizine", "Amoxicillin")
        comNametablet.current(0)
        comNametablet.grid(row=0, column=1)

        lblFurthreInfo = tk.Label(DataframeLeft, font=("arial", 12, "bold"), text="Further Info:", padx=2, pady=6)
        lblFurthreInfo.grid(row=0, column=2, sticky="w")
        txtFurthreInfo = tk.Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.FurtherInformation, width=35)
        txtFurthreInfo.grid(row=0, column=3)
        
        # Row 1
        lblref = tk.Label(DataframeLeft, font=("arial", 12, "bold"), text="Reference No:", padx=2)
        lblref.grid(row=1, column=0, sticky="w")
        txtref = tk.Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.ref, width=35)
        txtref.grid(row=1, column=1)
        
        lblBloodPressure = tk.Label(DataframeLeft, font=("arial", 12, "bold"), text="Blood Pressure:", padx=2, pady=6)
        lblBloodPressure.grid(row=1, column=2, sticky="w")
        txtBloodPressure = tk.Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.BloodPressure, width=35)
        txtBloodPressure.grid(row=1, column=3)
        
        # Row 2
        lblDose = tk.Label(DataframeLeft, font=("arial", 12, "bold"), text="Dose:", padx=2, pady=4)
        lblDose.grid(row=2, column=0, sticky="w")
        txtDose = tk.Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.Dose, width=35)
        txtDose.grid(row=2, column=1)
        
        lblStorage = tk.Label(DataframeLeft, font=("arial", 12, "bold"), text="Storage:", padx=2, pady=6)
        lblStorage.grid(row=2, column=2, sticky="w")
        txtStorage = tk.Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.StorageAdvice, width=35)
        txtStorage.grid(row=2, column=3)
        
        # Row 3
        lblNoofTablets = tk.Label(DataframeLeft, font=("arial", 12, "bold"), text="No of Tablets:", padx=2, pady=6)
        lblNoofTablets.grid(row=3, column=0, sticky="w")
        txtNoofTablets = tk.Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.NumberofTablets, width=35)
        txtNoofTablets.grid(row=3, column=1)

        lblMedication = tk.Label(DataframeLeft, font=("arial", 12, "bold"), text="Medication:", padx=2, pady=6)
        lblMedication.grid(row=3, column=2, sticky="w")
        txtMedication = tk.Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.HowToUseMedication, width=35)
        txtMedication.grid(row=3, column=3)
        
        # Row 4
        lblLot = tk.Label(DataframeLeft, font=("arial", 12, "bold"), text="Lot:", padx=2, pady=6)
        lblLot.grid(row=4, column=0, sticky="w")
        txtLot = tk.Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.Lot, width=35)
        txtLot.grid(row=4, column=1)
        
        lblPatientID = tk.Label(DataframeLeft, font=("arial", 12, "bold"), text="Patient ID:", padx=2, pady=6)
        lblPatientID.grid(row=4, column=2, sticky="w")
        txtPatientID = tk.Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.PatientId, width=35)
        txtPatientID.grid(row=4, column=3)

        # Row 5
        lblissueDate = tk.Label(DataframeLeft, font=("arial", 12, "bold"), text="Issue Date:", padx=2, pady=6)
        lblissueDate.grid(row=5, column=0, sticky="w")
        txtissueDate = tk.Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.Issuedate, width=35)
        txtissueDate.grid(row=5, column=1)
        
        lblNhsNumber = tk.Label(DataframeLeft, font=("arial", 12, "bold"), text="NHS Number:", padx=2, pady=6)
        lblNhsNumber.grid(row=5, column=2, sticky="w")
        txtNhsNumber = tk.Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.nhsNumber, width=35)
        txtNhsNumber.grid(row=5, column=3)

        # Row 6
        lblExpDate = tk.Label(DataframeLeft, font=("arial", 12, "bold"), text="Exp Date:", padx=2, pady=6)
        lblExpDate.grid(row=6, column=0, sticky="w")
        txtExpDate = tk.Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.ExpDate, width=35)
        txtExpDate.grid(row=6, column=1)
        
        lblPatientName = tk.Label(DataframeLeft, font=("arial", 12, "bold"), text="Patient Name:", padx=2, pady=6)
        lblPatientName.grid(row=6, column=2, sticky="w")
        txtPatientName = tk.Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.PatientName, width=35)
        txtPatientName.grid(row=6, column=3)

        # Row 7
        lblDailyDose = tk.Label(DataframeLeft, font=("arial", 12, "bold"), text="Daily Dose:", padx=2, pady=6)
        lblDailyDose.grid(row=7, column=0, sticky="w")
        txtDailyDose = tk.Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.DailyDose, width=35)
        txtDailyDose.grid(row=7, column=1)
        
        lblDateOfBirth = tk.Label(DataframeLeft, font=("arial", 12, "bold"), text="Date of Birth:", padx=2, pady=6)
        lblDateOfBirth.grid(row=7, column=2, sticky="w")
        txtDateOfBirth = tk.Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.DateOfBirth, width=35)
        txtDateOfBirth.grid(row=7, column=3)
        
        # Row 8
        lblSideEffect = tk.Label(DataframeLeft, font=("arial", 12, "bold"), text="Side Effect:", padx=2, pady=6)
        lblSideEffect.grid(row=8, column=0, sticky="w")
        txtSideEffect = tk.Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.SideEffect, width=35)
        txtSideEffect.grid(row=8, column=1)

        lblPatientAddress = tk.Label(DataframeLeft, font=("arial", 12, "bold"), text="Patient Address:", padx=2, pady=6)
        lblPatientAddress.grid(row=8, column=2, sticky="w")
        txtPatientAddress = tk.Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.PatientAddress, width=35)
        txtPatientAddress.grid(row=8, column=3)

        # ==================== DataFrameRight ====================
        self.textPrescription = tk.Text(DataframeRight, font=("arial", 12, "bold"), width=43, height=16, padx=2, pady=6)
        self.textPrescription.grid(row=0, column=0)

        # ==================== Buttons ====================
        btnPrescription = tk.Button(Buttonframe, text="Prescription", bg="blue", fg="white", font=("arial", 12, "bold"), width=24, command=self.generate_prescription)
        btnPrescription.grid(row=0, column=0)

        btnPrescriptionData = tk.Button(Buttonframe, text="Prescription Data", bg="blue", fg="white", font=("arial", 12, "bold"), width=24, command=self.iPrescriptionData)
        btnPrescriptionData.grid(row=0, column=1)

        btnUpdate = tk.Button(Buttonframe, text="Update", bg="blue", fg="white", font=("arial", 12, "bold"), width=24, command=self.update_data)
        btnUpdate.grid(row=0, column=2)

        btnDelete = tk.Button(Buttonframe, text="Delete", bg="blue", fg="white", font=("arial", 12, "bold"), width=24, command=self.delete_data)
        btnDelete.grid(row=0, column=3)

        btnClear = tk.Button(Buttonframe, text="Clear", bg="blue", fg="white", font=("arial", 12, "bold"), width=24, command=self.clear_fields)
        btnClear.grid(row=0, column=4)

        btnExit = tk.Button(Buttonframe, text="Exit", bg="blue", fg="white", font=("arial", 12, "bold"), width=24, command=self.root.quit)
        btnExit.grid(row=0, column=5)

        # ==================== Table & Scrollbars ====================
        scroll_x = tk.Scrollbar(Detailsframe, orient="horizontal")
        scroll_x.pack(side="bottom", fill="x")
        scroll_y = tk.Scrollbar(Detailsframe, orient="vertical")
        scroll_y.pack(side="right", fill="y")

        # 19 columns matching the SQL definition
        columns = (
            "nameoftablets", "ref", "dose", "nooftablets", "lot", "issuedate", "expdate", 
            "dailydose", "sideeffect", "furtherInfo", "storageadvice", "medication", 
            "patientId", "nhsnumber", "patientname", "dateofbirth", "patientaddress", 
            "bloodpressure" 
            # Note: DrivingUsingMachine is included in the prescription generator but not DB.
        )

        self.hospital_table = ttk.Treeview(
            Detailsframe,
            columns=columns,
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set,
            show="headings"
        )
        self.hospital_table.pack(fill="both", expand=1)

        scroll_x.config(command=self.hospital_table.xview)
        scroll_y.config(command=self.hospital_table.yview)

        for col in columns:
            self.hospital_table.heading(col, text=col.replace('_', ' ').title())
            self.hospital_table.column(col, width=120)

        self.hospital_table.bind("<<TreeviewSelect>>", self.on_row_selected)
        self.fetch_data()

    # ------------------ methods ------------------
    def clear_fields(self):
        """Clear all input fields"""
        self.Nameoftablets.set("")
        self.ref.set("")
        self.Dose.set("")
        self.NumberofTablets.set("")
        self.Lot.set("")
        self.Issuedate.set("")
        self.ExpDate.set("")
        self.DailyDose.set("")
        self.SideEffect.set("")
        self.FurtherInformation.set("")
        self.StorageAdvice.set("")
        self.DrivingUsingMachine.set("")
        self.HowToUseMedication.set("")
        self.PatientId.set("")
        self.nhsNumber.set("")
        self.PatientName.set("")
        self.DateOfBirth.set("")
        self.PatientAddress.set("")
        self.BloodPressure.set("") 
        self.textPrescription.delete("1.0", tk.END)

    def generate_prescription(self):
        self.textPrescription.delete("1.0", tk.END)

        self.textPrescription.configure(font=("Courier New", 12, "bold"))

        rows = [
            ("Tablet", self.Nameoftablets.get()),
            ("Reference No", self.ref.get()),
            ("Dose", self.Dose.get()),
            ("No of Tablets", self.NumberofTablets.get()),
            ("Lot", self.Lot.get()),
            ("Issue Date", self.Issuedate.get()),
            ("Exp Date", self.ExpDate.get()),
            ("Daily Dose", self.DailyDose.get()),
            ("Side Effect", self.SideEffect.get()),
            ("Further Info", self.FurtherInformation.get()),
            ("Blood Pressure", self.BloodPressure.get()), 
            ("Storage", self.StorageAdvice.get()),
            ("Driving/Machines", self.DrivingUsingMachine.get()),
            ("Medication Use", self.HowToUseMedication.get()),
            ("Patient ID", self.PatientId.get()),
            ("NHS Number", self.nhsNumber.get()),
            ("Patient Name", self.PatientName.get()),
            ("Date of Birth", self.DateOfBirth.get()),
            ("Address", self.PatientAddress.get())
        ]

        colon_index = 16
        lines = []

        for label, value in rows:
            padded_label = label.ljust(colon_index)
            line = f"{padded_label}: {value}"
            lines.append(line)

        self.textPrescription.insert(tk.END, "\n".join(lines))


    def get_connection(self):
        return mysql.connector.connect(**self.db_config)

    def iPrescriptionData(self):
        if self.Nameoftablets.get()=="" or self.ref.get()=="":
            messagebox.showerror("Error","All Fields are Required")
            return

        try:
            conn = self.get_connection()
            my_cursor = conn.cursor()

            insert_query = """
            INSERT INTO data (
                nameoftablets, ref, dose, nooftablets, lot, issuedate, expdate, dailydose,
                sideeffect, furtherInfo, bloodpressure, storageadvice, medication,
                patientId, nhsnumber, patientname, dateofbirth, patientaddress
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """

            values = (
                self.Nameoftablets.get(),
                self.ref.get(),
                self.Dose.get(),
                self.NumberofTablets.get(),
                self.Lot.get(),
                self.Issuedate.get(),
                self.ExpDate.get(),
                self.DailyDose.get(),
                self.SideEffect.get(),
                self.FurtherInformation.get(),
                self.BloodPressure.get(),
                self.StorageAdvice.get(),
                self.HowToUseMedication.get(),
                self.PatientId.get(),
                self.nhsNumber.get(),
                self.PatientName.get(),
                self.DateOfBirth.get(),
                self.PatientAddress.get()
            )

            my_cursor.execute(insert_query, values)
            conn.commit()
            messagebox.showinfo("Success", "Record inserted successfully")
            self.fetch_data()

        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Error: {e}")

        finally:
            try:
                my_cursor.close()
                conn.close()
            except:
                pass


    def fetch_data(self):
        try:
            conn = self.get_connection()
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM data")
            rows = my_cursor.fetchall()

            # MUST CLEAR TREEVIEW BEFORE RELOADING
            self.hospital_table.delete(*self.hospital_table.get_children())

            for row in rows:
                self.hospital_table.insert("", tk.END, values=row)

        except Exception as e:
            messagebox.showerror("Error", str(e))

        finally:
            try:
                my_cursor.close()
                conn.close()
            except:
                pass



    def on_row_selected(self, event=""):
        selected = self.hospital_table.focus()
        values = self.hospital_table.item(selected, "values")

        if values == "" or len(values) < 18:
            return

        self.Nameoftablets.set(values[0])
        self.ref.set(values[1])
        self.Dose.set(values[2])
        self.NumberofTablets.set(values[3])
        self.Lot.set(values[4])
        self.Issuedate.set(values[5])
        self.ExpDate.set(values[6])
        self.DailyDose.set(values[7])
        self.SideEffect.set(values[8])
        self.FurtherInformation.set(values[9])
        self.BloodPressure.set(values[10])
        self.StorageAdvice.set(values[11])
        self.HowToUseMedication.set(values[12])
        self.PatientId.set(values[13])
        self.nhsNumber.set(values[14])
        self.PatientName.set(values[15])
        self.DateOfBirth.set(values[16])
        self.PatientAddress.set(values[17])

        
#---------------------------------------------------------------------------------------------------
    def update_data(self):
        if self.ref.get().strip() == "":
            messagebox.showerror("Error", "Reference No is required to update a record.")
            return

        try:
            conn = self.get_connection()
            my_cursor = conn.cursor()

            update_query = """
            UPDATE data SET
                nameoftablets=%s,
                dose=%s,
                nooftablets=%s,
                lot=%s,
                issuedate=%s,
                expdate=%s,
                dailydose=%s,
                sideeffect=%s,
                furtherInfo=%s,
                bloodpressure=%s,
                storageadvice=%s,
                medication=%s,
                patientId=%s,
                nhsnumber=%s,
                patientname=%s,
                dateofbirth=%s,
                patientaddress=%s
            WHERE ref=%s
            """

            values = (
                self.Nameoftablets.get(),
                self.Dose.get(),
                self.NumberofTablets.get(),
                self.Lot.get(),
                self.Issuedate.get(),
                self.ExpDate.get(),
                self.DailyDose.get(),
                self.SideEffect.get(),
                self.FurtherInformation.get(),
                self.BloodPressure.get(),
                self.StorageAdvice.get(),
                self.HowToUseMedication.get(),
                self.PatientId.get(),
                self.nhsNumber.get(),
                self.PatientName.get(),
                self.DateOfBirth.get(),
                self.PatientAddress.get(),
                self.ref.get()
            )

            my_cursor.execute(update_query, values)
            conn.commit()

            messagebox.showinfo("Success", "Record updated successfully")
            self.fetch_data()

        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Error: {e}")

        finally:
            try:
                my_cursor.close()
                conn.close()
            except:
                pass

#---------------------------------------------------------------------------------------------------
    def delete_data(self):
        if self.ref.get().strip() == "":
            messagebox.showerror("Error", "Reference No is required to delete a record.")
            return

        try:
            # Selected row from treeview
            selected_item = self.hospital_table.focus()

            conn = self.get_connection()
            my_cursor = conn.cursor()

            # Delete from SQL
            my_cursor.execute("DELETE FROM data WHERE ref=%s", (self.ref.get(),))
            conn.commit()

            # Delete from UI instantly
            if selected_item:
                self.hospital_table.delete(selected_item)

            # Clear all fields
            self.clear_fields()

            messagebox.showinfo("Deleted", "Record deleted successfully")

            # Reload full data (safe refresh)
            self.fetch_data()

        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Error: {e}")

        finally:
            try:
                my_cursor.close()
                conn.close()
            except:
                pass



if __name__ == "__main__":
    root = tk.Tk()
    app = Hospital(root)

    root.mainloop()

