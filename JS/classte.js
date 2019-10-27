class ClassWithStaticField {
    static baseStaticField = 'base field';
}

class SubClassWithStaticField extends ClassWithStaticField {
    static subStaticField = 'sub class field';

    static fds(params) {
        console.log(this.subStaticField)
    }


}


SubClassWithStaticField.fds()
// 预期输出值: "base field"



const PREFIX = 'prefix';

class ClassWithComputedFieldName {
    [`${PREFIX}Field`] = 'prefixed field';
}   

const instance = new ClassWithComputedFieldName();
console.log(instance.prefixField);
console.log([`${PREFIX}Field`]);
