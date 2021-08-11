var app1 = new Vue({
    el: '#app-1',
    data:{
        message: "여기를 수정해보세요"
    }
});

var app2 = new Vue({
    el: '#app-2',
    data:{
        message: "여러줄을 입력해보세요"
    }
})

var app3 = new Vue({
    el: '#app-3',
    data:{
        checked: false
    }
})

var app4 = new Vue({
    el: '#app-4',
    data:{
        checkedNames: []
    }
})

var app5 = new Vue({
    el: '#app-5',
    data:{
        picked: ''
    }
})

var app6 = new Vue({
    el: '#app-6',
    data:{
        selected: ''
    }
})

var app7 = new Vue({
    el: '#app-7',
    data:{
        selected: ''
    }
})

var app8 = new Vue({
    el: '#app-8',
    data: {
        selected: 'A',
        options: [
            {text: 'One', value: 'A'},
            {text: 'Two', value: 'B'},
            {text: 'Three', value: 'C'}
        ]
    }
})

var app9 = new Vue({
    el: '#app-9',
    data: {
        toggle: 'no'
    }
})

var app10 = new Vue({
    el: '#app-10',
    data: {
        pick: '',
        a: '짜짠!?'
    }
})

var app11 = new Vue({
    el: '#app-11',
    data: {
        selected: ''
    }
})

var app12 = new Vue({
    el: '#app-12',
    data: {
        msg: '입력이 다 되면 변경됨'
    }
})

var app13 = new Vue({
    el: '#app-13',
    data: {
        age: 0
    }
})

var app14 = new Vue({
    el: '#app-14',
    data: {
        msg: ''
    }
})

/*
    Prop 검증 부분
    Vue.component('example', {
        props: {
            // 기본 타입 확인 (`null` 은 어떤 타입이든 가능하다는 뜻입니다)
            propA: Number,
            // 여러개의 가능한 타입
            propB: [String, Number],
            // 문자열이며 꼭 필요합니다
            propC: {
                type: String,
                required: true
            },
            // 숫자이며 기본 값을 가집니다
            propD: {
                type: Number,
                default: 100
            },
            // 객체/배열의 기본값은 팩토리 함수에서 반환 되어야 합니다.
            propE: {
                type: Object,
                default: function () {
                    return { message: 'hello' }
                }
            },
            // 사용자 정의 유효성 검사 가능
            propF: {
                validator: function (value) {
                    return value > 10
                }
            }
        }
    })
*/

Vue.component('button-counter',{
    template: '<button v-on:click="incrementCounter">{{counter}}</button>',
    data: function(){
        return {counter: 0}
    },
    methods: {
        incrementCounter: function(){
            this.counter += 1
            this.$emit('increment')
        }
    }
})

var app15 = new Vue({
    el: '#app-15',
    data: {
        total: 0
    },
    methods: {
        incrementTotal: function(){
            this.total += 1
        }
    }
})

Vue.component('currency-input', {
    template: '\
      <div>\
        <label v-if="label">{{ label }}</label>\
        $\
        <input\
          ref="input"\
          v-bind:value="value"\
          v-on:input="updateValue($event.target.value)"\
          v-on:focus="selectAll"\
          v-on:blur="formatValue"\
        >\
      </div>\
    ',
    props: {
      value: { type: Number, default: 0 },
      label: { type: String, default: ''}
    },
    mounted: function () {
      this.formatValue()
    },
    methods: {
      updateValue: function (value) {
        var result = currencyValidator.parse(value, this.value)
        if (result.warning) {
          this.$refs.input.value = result.value
        }
        this.$emit('input', result.value)
      },
      formatValue: function () {
        this.$refs.input.value = currencyValidator.format(this.value)
      },
      selectAll: function (event) {
        // Workaround for Safari bug
        // http://stackoverflow.com/questions/1269722/selecting-text-on-focus-using-jquery-not-working-in-safari-and-chrome
        setTimeout(function () {
            event.target.select()
        }, 0)
      }
    }
  })
var app16 = new Vue({
    el: '#app-16',
    data: {
      price: 0,
      shipping: 0,
      handling: 0,
      discount: 0
    },
    computed: {
      total: function () {
        return ((
          this.price * 100 + 
          this.shipping * 100 + 
          this.handling * 100 - 
          this.discount * 100
        ) / 100).toFixed(2)
      }
    }
})
