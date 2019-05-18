import patientClass
import procedureClass


def procedure():
    name = input('Enter the name of the procedure: ')
    date = input('Enter the date when the procedure was performed: ')
    name_practitioner = input('Enter the name of the practitioner who performed the procedure: ')
    charges = input('Enter the charges for the procedure: ')
    obj = procedureClass.Procedure(name, date, name_practitioner, charges)
    return obj


def procedure_info():
    print('Procedure 1')
    obj1 = procedure()
    print('Procedure 2')
    obj2 = procedure()
    print('Procedure 3')
    obj3 = procedure()

    return obj1, obj2, obj3


def print_procedure_info(obj):
    print('Name of procedure:', obj.get_name())
    print('Date of procedure:', obj.get_date())
    print('Practitioner Name:', obj.get_name_practitioner())
    print('Charges:', obj.get_charges())
    print('\n')


def patient_info():
    name = input('Enter the full name of the patient(First name followed by middle and last name): ')
    address = input('Enter full address with city, state and zip code: ')
    phone = input('Enter the phone number: ')
    emergency = input('Enter the name and phone number of the emergency contact: ')
    obj = patientClass.Patient(name, address, phone, emergency)
    obj1, obj2, obj3 = procedure_info()
    print('\n')
    print('Patient info')
    print('Name:', obj.get_name())
    print('Address:', obj.get_address())
    print('Phone:', obj.get_phone())
    print('Emergency Contact:', obj.get_emergency())
    print('\n')
    print('Procedure 1 info')
    print_procedure_info(obj1)
    print('Procedure 2 info')
    print_procedure_info(obj2)
    print('Procedure 3 info')
    print_procedure_info(obj3)
    total_charges = format(float(obj1.get_charges()) + float(obj2.get_charges()) + float(obj3.get_charges()), '.2f')
    print('Total charges for all three procedures: $', total_charges)


def main():
    patient_info()


main()