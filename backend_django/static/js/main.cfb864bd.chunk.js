(window.webpackJsonp=window.webpackJsonp||[]).push([[0],{151:function(e,t,a){},165:function(e,t){},166:function(e,t){},167:function(e,t){},172:function(e,t,a){e.exports=a(384)},177:function(e,t,a){},181:function(e,t,a){},230:function(e,t,a){},236:function(e,t,a){},256:function(e,t,a){},267:function(e,t,a){},269:function(e,t,a){e.exports=a.p+"static/media/logo.5d5d9eef.svg"},270:function(e,t,a){},309:function(e,t,a){},375:function(e,t,a){},380:function(e,t,a){},382:function(e,t,a){},384:function(e,t,a){"use strict";a.r(t);var n=a(2),l=a.n(n),r=a(152),i=a.n(r),c=(a(177),a(78),a(28)),o=(a(79),a(14)),s=a(15),u=a(16),m=a(18),h=a(17),d=a(19),p=(a(181),function(e){if(!e)return"";var t=new Date(e);return t.getFullYear()+"-"+t.getMonth()+"1-"+t.getDate()+"          "+t.getHours()+":"+t.getMinutes()+":"+t.getSeconds()+"          "}),E=function(e){function t(){var e,a;Object(s.a)(this,t);for(var n=arguments.length,l=new Array(n),r=0;r<n;r++)l[r]=arguments[r];return(a=Object(m.a)(this,(e=Object(h.a)(t)).call.apply(e,[this].concat(l)))).state={},a}return Object(d.a)(t,e),Object(u.a)(t,[{key:"componentWillMount",value:function(){var e=this;setInterval(function(){var t=p((new Date).getTime());e.setState({sysTime:t})},1e3)}},{key:"render",value:function(){return l.a.createElement("div",{className:"header"},l.a.createElement(c.a,{className:"top"},l.a.createElement(o.a,{span:"24",classname:"title"},l.a.createElement("span",null,"\u8bd5\u5377\u667a\u80fd\u751f\u6210\u53ca\u9898\u5e93\u7ba1\u7406\u7cfb\u7edf"))),l.a.createElement(c.a,{className:"bread"},l.a.createElement(o.a,{span:"4"}),l.a.createElement(o.a,{span:"20",classname:"data-weather"},l.a.createElement("span",{className:"data"},this.state.sysTime),l.a.createElement("span",{className:"weather"},"\u6674"))))}}]),t}(l.a.Component),g=(a(230),function(e){function t(){return Object(s.a)(this,t),Object(m.a)(this,Object(h.a)(t).apply(this,arguments))}return Object(d.a)(t,e),Object(u.a)(t,[{key:"render",value:function(){return l.a.createElement("div",{className:"footer"},"\u7248\u6743\u6240\u6709\uff1a\u5357\u4eac\u822a\u7a7a\u822a\u5929\u5927\u5b66 \u8054\u7cfb\u6211\u4eec\uff1aptyhyt@foxmail.com TEl\uff1a17721571129")}}]),t}(l.a.Component)),f=(a(386),a(98)),b=[{tit1e:"\u9996\u9875",key:"/admin"},{tit1e:"\u8bd5\u5377\u667a\u80fd\u751f\u6210\u7cfb\u7edf",key:"/admin/paper",children:[{tit1e:"\u751f\u6210\u8bd5\u5377",key:"/admin/paper/makepaper"},{tit1e:"\u5386\u53f2\u8bd5\u5377\u8bb0\u5f55",key:"/admin/paper/history"}]},{tit1e:"\u9898\u5e93\u7ba1\u7406\u7cfb\u7edf",key:"/admin/question",children:[{tit1e:"\u4e0a\u4f20\u8bd5\u9898",key:"/admin/question/upload"},{tit1e:"\u8bd5\u9898\u7ba1\u7406",key:"/admin/question/manage"}]}],v=a(389),y=(a(236),f.a.SubMenu),C=function(e){function t(){var e,a;Object(s.a)(this,t);for(var n=arguments.length,r=new Array(n),i=0;i<n;i++)r[i]=arguments[i];return(a=Object(m.a)(this,(e=Object(h.a)(t)).call.apply(e,[this].concat(r)))).renderMenu=function(e){return e.map(function(e){return e.children?l.a.createElement(y,{title:e.tit1e,key:e.key,color:"#ffffff"},a.renderMenu(e.children)):l.a.createElement(f.a.Item,{title:e.tit1e,key:e.key},l.a.createElement(v.a,{to:e.key},e.tit1e))})},a}return Object(d.a)(t,e),Object(u.a)(t,[{key:"componentWillMount",value:function(){var e=this.renderMenu(b);this.setState({menuTreeNode:e})}},{key:"render",value:function(){return l.a.createElement("div",null,l.a.createElement("div",{className:"logo"},l.a.createElement("h1",{className:"h1"},"NUAA")),l.a.createElement(f.a,{theme:"dark"},this.state.menuTreeNode))}}]),t}(l.a.Component),j=(a(253),a(169)),O=(a(256),function(e){function t(){var e,a;Object(s.a)(this,t);for(var n=arguments.length,l=new Array(n),r=0;r<n;r++)l[r]=arguments[r];return(a=Object(m.a)(this,(e=Object(h.a)(t)).call.apply(e,[this].concat(l)))).state={value:3},a.handleChange=function(e){a.setState({value:e})},a}return Object(d.a)(t,e),Object(u.a)(t,[{key:"render",value:function(){var e=this.state.value;return l.a.createElement("div",null,l.a.createElement("div",{className:"homepage"},l.a.createElement("h1",null,"\u6b22\u8fce\u4f7f\u7528\u8bd5\u5377\u81ea\u52a8\u751f\u6210\u53ca\u9898\u5e93\u7ba1\u7406\u7cfb\u7edf"),l.a.createElement("p1",null,"\u672c\u7cfb\u7edf\u5f00\u53d1from\uff1a\u5357\u4eac\u822a\u7a7a\u822a\u5929\u5927\u5b66\u8ba1\u7b97\u673a\u79d1\u5b66\u4e0e\u6280\u672f\u5b66\u966215\u7ea7\u8f6f\u4ef6\u5de5\u7a0b\u7efc\u5408\u8bfe\u7a0b\u8bbe\u8ba1"),l.a.createElement("div",null,"\u524d\u7aef\u5f00\u53d1\u8005\uff1a\u738b\u4ee4\u9633\uff0c\u88f4\u5929\u9633"),l.a.createElement("div",null,"\u540e\u7aef\u5f00\u53d1\u8005\uff1a\u8c22\u4e91\u8f69\uff0c\u738b\u5929\u884c"),l.a.createElement("div",null,"\u7b97\u6cd5\u652f\u6301\uff1a\u738b\u5929\u884c"),l.a.createElement("div",null,"\u5982\u679c\u60a8\u5728\u4f7f\u7528\u8fc7\u7a0b\u4e2d\u51fa\u73b0\u95ee\u9898\u53ef\u4ee5\u968f\u65f6\u8054\u7cfb\u6211\u4eec")),l.a.createElement("div",{className:"grade"},l.a.createElement("div",null,"\u5982\u679c\u5728\u4f7f\u7528\u8fc7\u7a0b\u4e2d\u611f\u89c9\u4e0d\u9519\u53ef\u4ee5\u4e3a\u6211\u4eec\u8fdb\u884c\u6253\u5206"),l.a.createElement("span",null,l.a.createElement(j.a,{onChange:this.handleChange,value:e}),e&&l.a.createElement("span",{className:"ant-rate-text"},e," stars")),l.a.createElement("div",null,"\u5341\u5206\u611f\u8c22\u60a8\u7684\u53cd\u9988")))}}]),t}(l.a.Component)),w=(a(267),function(e){function t(){return Object(s.a)(this,t),Object(m.a)(this,Object(h.a)(t).apply(this,arguments))}return Object(d.a)(t,e),Object(u.a)(t,[{key:"render",value:function(){return l.a.createElement(c.a,{className:"container"},l.a.createElement(o.a,{span:"4",className:"menu"},l.a.createElement(C,null)),l.a.createElement(o.a,{span:"20",className:"main"},l.a.createElement(E,null),l.a.createElement(c.a,{className:"content"},this.props.children),l.a.createElement(g,null)))}}]),t}(l.a.Component)),k=a(388),q=a(387),S=a(390),N=(a(269),a(270),function(e){function t(){return Object(s.a)(this,t),Object(m.a)(this,Object(h.a)(t).apply(this,arguments))}return Object(d.a)(t,e),Object(u.a)(t,[{key:"render",value:function(){return l.a.createElement("div",{className:"App"},this.props.children)}}]),t}(n.Component)),A=(a(45),a(13)),U=(a(385),a(168)),V=(a(61),a(24)),D=(a(62),a(27)),x=(a(73),a(36)),B=(a(75),a(29)),L=a(33),M=a.n(L),T=a(34),F=a.n(T),Q=a(20),I=a.n(Q),Y=(a(309),B.a.Item,x.a.Group,function(e){function t(){var e,a;Object(s.a)(this,t);for(var n=arguments.length,l=new Array(n),r=0;r<n;r++)l[r]=arguments[r];return(a=Object(m.a)(this,(e=Object(h.a)(t)).call.apply(e,[this].concat(l)))).state={loading:!1,repetition:"0",subject:"\u6570\u636e\u7ed3\u6784",calculation:"1,2,3",shortanswer:"1,2,3",date:"2019/01/01",word:""},a.onRepetitionChange=function(e){a.setState({repetition:e.target.value})},a.onSubjectChange=function(e){a.setState({subject:e.target.value})},a.onCalculationChange=function(e){a.setState({calculation:e.target.value})},a.onShortanswerChange=function(e){a.setState({shortanswer:e.target.value})},a.onDateChange=function(e){a.setState({date:e.target.value})},a.enterLoading=function(){a.setState({loading:!0});F.a.post("http://localhost:8000/request/make",M.a.stringify({repetition:a.state.repetition,subject:a.state.subject,calculation:a.state.calculation,shortanswer:a.state.shortanswer,date:a.state.date})).then(function(e){"114514"==e.data?(D.a.success("\u751f\u6210\u6210\u529f!"),a.setState({loading:!1})):(D.a.error("\u751f\u6210\u5931\u8d25!!"),a.setState({loading:!1}))})},a.closeLoading=function(){a.setState({loading:!1})},a}return Object(d.a)(t,e),Object(u.a)(t,[{key:"render",value:function(){return l.a.createElement("div",{className:"homepage"},l.a.createElement("div",{style:{marginBottom:16},className:"input"},l.a.createElement(V.a,{addonBefore:"\u91cd\u590d\u7387\u8981\u6c42\u4e0d\u8d85\u8fc7",addonAfter:"%",defaultValue:this.state.repetition,onChange:this.onRepetitionChange}),l.a.createElement("br",null),l.a.createElement("br",null),l.a.createElement(V.a,{addonBefore:"\u79d1\u76ee",defaultValue:this.state.subject,onChange:this.onSubjectChange}),l.a.createElement("br",null),l.a.createElement("br",null),l.a.createElement(V.a,{addonBefore:"\u8ba1\u7b97\u9898\u5355\u5143\u8003\u5bdf",defaultValue:this.state.calculation,onChange:this.onCalculationChange}),l.a.createElement("br",null),l.a.createElement("br",null),l.a.createElement(V.a,{addonBefore:"\u7b80\u7b54\u9898\u5355\u5143\u8003\u5bdf",defaultValue:this.state.shortanswer,onChange:this.onShortanswerChange}),l.a.createElement("br",null),l.a.createElement("br",null),l.a.createElement(U.a,{defaultValue:I()("2019/01/01","YYYY/MM/DD"),format:"YYYY/MM/DD",onChange:this.onDateChange})),l.a.createElement(A.a,{type:"primary",onClick:this.enterLoading},"\u751f\u6210\u8bd5\u5377"),l.a.createElement(A.a,{icon:"download",href:"http://localhost:8000/public/assets"},"\u4e0b\u8f7d\u8bd5\u5377"),l.a.createElement(A.a,{icon:"download",href:"http://localhost:8000/public/answer"},"\u4e0b\u8f7d\u7b54\u6848"))}}]),t}(l.a.Component)),W=(a(68),a(35)),G=(a(375),function(e){function t(){var e,a;Object(s.a)(this,t);for(var n=arguments.length,l=new Array(n),r=0;r<n;r++)l[r]=arguments[r];return(a=Object(m.a)(this,(e=Object(h.a)(t)).call.apply(e,[this].concat(l)))).state={time1:"",time2:"",time3:""},a}return Object(d.a)(t,e),Object(u.a)(t,[{key:"componentWillMount",value:function(){var e=this;F.a.post("http://localhost:8000/time",M.a.stringify({time:this.state.time1})).then(function(t){""!=t.data?e.setState({time1:t.data.time1,time2:t.data.time2,time3:t.data.time3}):D.a.error("\u83b7\u53d6\u5931\u8d25!!")})}},{key:"render",value:function(){return l.a.createElement("div",{className:"homepage"},l.a.createElement(W.a,{className:"iquestion"},l.a.createElement(c.a,null,l.a.createElement(o.a,{span:"18"},l.a.createElement("p",null,"\u751f\u6210\u65f6\u95f4\uff1a",this.state.time1)),l.a.createElement(o.a,{span:"3"},l.a.createElement("div",{className:"ibutton1"},l.a.createElement(A.a,{icon:"download",href:"http://localhost:8000/paper/question1"},"\u4e0b\u8f7d\u8bd5\u5377"))),l.a.createElement(o.a,{span:"3"},l.a.createElement("div",{className:"ibutton2"},l.a.createElement(A.a,{icon:"download",href:"http://localhost:8000/paper/answer1"},"\u4e0b\u8f7d\u7b54\u6848"))))),l.a.createElement("br",null),l.a.createElement(W.a,{className:"iquestion"},l.a.createElement(c.a,null,l.a.createElement(o.a,{span:"18"},l.a.createElement("p",null,"\u751f\u6210\u65f6\u95f4\uff1a",this.state.time2)),l.a.createElement(o.a,{span:"3"},l.a.createElement("div",{className:"ibutton1"},l.a.createElement(A.a,{icon:"download",href:"http://localhost:8000/paper/question2"},"\u4e0b\u8f7d\u8bd5\u5377"))),l.a.createElement(o.a,{span:"3"},l.a.createElement("div",{className:"ibutton2"},l.a.createElement(A.a,{icon:"download",href:"http://localhost:8000/paper/answer2"},"\u4e0b\u8f7d\u7b54\u6848"))))),l.a.createElement("br",null),l.a.createElement(W.a,{className:"iquestion"},l.a.createElement(c.a,null,l.a.createElement(o.a,{span:"18"},l.a.createElement("p",null,"\u751f\u6210\u65f6\u95f4\uff1a",this.state.time3)),l.a.createElement(o.a,{span:"3"},l.a.createElement("div",{className:"ibutton1"},l.a.createElement(A.a,{icon:"download",href:"http://localhost:8000/paper/question3"},"\u4e0b\u8f7d\u8bd5\u5377"))),l.a.createElement(o.a,{span:"3"},l.a.createElement("div",{className:"ibutton2"},l.a.createElement(A.a,{icon:"download",href:"http://localhost:8000/paper/answer3"},"\u4e0b\u8f7d\u7b54\u6848"))))))}}]),t}(l.a.Component)),J=(a(151),function(e){function t(){return Object(s.a)(this,t),Object(m.a)(this,Object(h.a)(t).apply(this,arguments))}return Object(d.a)(t,e),Object(u.a)(t,[{key:"render",value:function(){return l.a.createElement("div",{className:"homepage"},l.a.createElement(v.a,{to:"./display/choice"},l.a.createElement(A.a,null," \u9009\u62e9\u9898 ")),l.a.createElement(v.a,{to:"./display/blank"},l.a.createElement(A.a,null," \u586b\u7a7a\u9898 ")),l.a.createElement(v.a,{to:"./display/calculation"},l.a.createElement(A.a,null," \u8ba1\u7b97\u9898 ")),l.a.createElement(v.a,{to:"./display/shortanswer"},l.a.createElement(A.a,null," \u7b80\u7b54\u9898 ")))}}]),t}(l.a.Component)),R=function(e){function t(){return Object(s.a)(this,t),Object(m.a)(this,Object(h.a)(t).apply(this,arguments))}return Object(d.a)(t,e),Object(u.a)(t,[{key:"render",value:function(){return l.a.createElement("div",{className:"homepage"},l.a.createElement(v.a,{to:"./manage/choice"},l.a.createElement(A.a,null," \u9009\u62e9\u9898 ")),l.a.createElement(v.a,{to:"./manage/blank"},l.a.createElement(A.a,null," \u586b\u7a7a\u9898 ")),l.a.createElement(v.a,{to:"./manage/calculation"},l.a.createElement(A.a,null," \u8ba1\u7b97\u9898 ")),l.a.createElement(v.a,{to:"./manage/shortanswer"},l.a.createElement(A.a,null," \u7b80\u7b54\u9898 ")))}}]),t}(l.a.Component),H=(a(380),function(e){function t(){return Object(s.a)(this,t),Object(m.a)(this,Object(h.a)(t).apply(this,arguments))}return Object(d.a)(t,e),Object(u.a)(t,[{key:"render",value:function(){return l.a.createElement("div",null,l.a.createElement("div",null,"this is questionsdisplay page."),l.a.createElement(v.a,{to:"./manage"},l.a.createElement(A.a,{icon:"left",type:"primary"},"\u8fd4\u56de")))}}]),t}(l.a.Component)),$=B.a.Item,z=x.a.Group,K=function(e){function t(){var e,a;Object(s.a)(this,t);for(var n=arguments.length,l=new Array(n),r=0;r<n;r++)l[r]=arguments[r];return(a=Object(m.a)(this,(e=Object(h.a)(t)).call.apply(e,[this].concat(l)))).state={title:"",bodyA:"",bodyB:"",bodyC:"",bodyD:"",Unit:"",value:"2"},a.onTitleChange=function(e){a.setState({title:e.target.value})},a.onAChange=function(e){a.setState({bodyA:e.target.value})},a.onBChange=function(e){a.setState({bodyB:e.target.value})},a.onCChange=function(e){a.setState({bodyC:e.target.value})},a.onDChange=function(e){a.setState({bodyD:e.target.value})},a.onUnitChange=function(e){a.setState({Unit:e.target.value})},a.enterLoading=function(){a.props.form.getFieldsValue();a.props.form.validateFields(function(e,t){if(!e)F.a.post("http://localhost:8000/request/choice",M.a.stringify({title:a.state.title,bodyA:a.state.bodyA,bodyB:a.state.bodyB,bodyC:a.state.bodyC,bodyD:a.state.bodyD,Unit:a.state.Unit,value:a.state.value})).then(function(e){"114514"==e.data?D.a.success("\u4e0a\u4f20\u6210\u529f!"):D.a.error("\u4e0a\u4f20\u5931\u8d25!!")})})},a.closeLoading=function(){a.setState({loading:!1})},a.onChange=function(e){console.log("radio checked",e.target.value),a.setState({value:e.target.value})},a}return Object(d.a)(t,e),Object(u.a)(t,[{key:"render",value:function(){var e=this.props.form.getFieldDecorator;return l.a.createElement("div",null,l.a.createElement(W.a,{title:"\u9009\u62e9\u9898"},l.a.createElement(B.a,null,l.a.createElement($,null,e("question",{initialValue:"",rules:[{required:!0,message:"\u4e0d\u53ef\u4ee5\u5b58\u5728\u7a7a\u7684\u9898\u76ee"}]})(l.a.createElement(V.a,{placeholder:"\u8bf7\u8f93\u5165\u9898\u5e72",onChange:this.onTitleChange}))),l.a.createElement($,null,e("A",{initialValue:"",rules:[{required:!0,message:"\u4e0d\u53ef\u4ee5\u5b58\u5728\u7a7a\u7684\u9009\u9879"}]})(l.a.createElement(V.a,{placeholder:"\u8bf7\u8f93\u5165\u9009\u9879A",onChange:this.onAChange}))),l.a.createElement($,null,e("B",{initialValue:"",rules:[{required:!0,message:"\u4e0d\u53ef\u4ee5\u5b58\u5728\u7a7a\u7684\u9009\u9879"}]})(l.a.createElement(V.a,{placeholder:"\u8bf7\u8f93\u5165\u9009\u9879B",onChange:this.onBChange}))),l.a.createElement($,null,e("C",{initialValue:"",rules:[{required:!0,message:"\u4e0d\u53ef\u4ee5\u5b58\u5728\u7a7a\u7684\u9009\u9879"}]})(l.a.createElement(V.a,{placeholder:"\u8bf7\u8f93\u5165\u9009\u9879C",onChange:this.onCChange}))),l.a.createElement($,null,e("D",{initialValue:"",rules:[{required:!0,message:"\u4e0d\u53ef\u4ee5\u5b58\u5728\u7a7a\u7684\u9009\u9879"}]})(l.a.createElement(V.a,{placeholder:"\u8bf7\u8f93\u5165\u9009\u9879D",onChange:this.onDChange}))),l.a.createElement($,null,e("Unit",{initialValue:"",rules:[{required:!0,message:"\u4e0d\u53ef\u4ee5\u5b58\u5728\u7a7a\u7684\u6240\u5c5e\u5355\u5143"}]})(l.a.createElement(V.a,{placeholder:"\u8bf7\u8f93\u5165\u6240\u5c5e\u5355\u5143",onChange:this.onUnitChange}))),l.a.createElement($,null,l.a.createElement("p",null,"\u6b63\u786e\u7b54\u6848\uff1a"),l.a.createElement(z,{onChange:this.onChange,value:this.state.value},l.a.createElement(x.a,{value:1},"A"),l.a.createElement(x.a,{value:2},"B"),l.a.createElement(x.a,{value:3},"C"),l.a.createElement(x.a,{value:4},"D")),l.a.createElement("br",null),l.a.createElement(A.a,{icon:"upload",type:"primary",loading:this.state.loading,onClick:this.enterLoading},"\u4e0a\u4f20")))))}}]),t}(l.a.Component),P=B.a.create()(K),X=B.a.Item,Z=(x.a.Group,function(e){function t(){var e,a;Object(s.a)(this,t);for(var n=arguments.length,l=new Array(n),r=0;r<n;r++)l[r]=arguments[r];return(a=Object(m.a)(this,(e=Object(h.a)(t)).call.apply(e,[this].concat(l)))).state={title:"",answer:"",Unit:""},a.onTitleChange=function(e){a.setState({title:e.target.value})},a.onAnswerChange=function(e){a.setState({answer:e.target.value})},a.onUnitChange=function(e){a.setState({Unit:e.target.value})},a.enterLoading=function(){a.props.form.getFieldsValue();a.props.form.validateFields(function(e,t){if(!e)F.a.post("http://localhost:8000/request/blank",M.a.stringify({title:a.state.title,Unit:a.state.Unit,answer:a.state.answer})).then(function(e){"114514"==e.data?D.a.success("\u4e0a\u4f20\u6210\u529f!"):D.a.error("\u4e0a\u4f20\u5931\u8d25!!")})})},a.closeLoading=function(){a.setState({loading:!1})},a}return Object(d.a)(t,e),Object(u.a)(t,[{key:"render",value:function(){var e=this.props.form.getFieldDecorator;return l.a.createElement("div",null,l.a.createElement(W.a,{title:"\u586b\u7a7a\u9898"},l.a.createElement(B.a,null,l.a.createElement(X,null,e("question",{initialValue:"",rules:[{required:!0,message:"\u4e0d\u53ef\u4ee5\u5b58\u5728\u7a7a\u7684\u9898\u76ee"}]})(l.a.createElement(V.a,{placeholder:"\u8bf7\u8f93\u5165\u9898\u5e72",onChange:this.onTitleChange}))),l.a.createElement(X,null,e("Unit",{initialValue:"",rules:[{required:!0,message:"\u4e0d\u53ef\u4ee5\u5b58\u5728\u7a7a\u7684\u6240\u5c5e\u5355\u5143"}]})(l.a.createElement(V.a,{placeholder:"\u8bf7\u8f93\u5165\u6240\u5c5e\u5355\u5143",onChange:this.onUnitChange}))),l.a.createElement(X,null,l.a.createElement("p",null,"\u6b63\u786e\u7b54\u6848\uff1a")),l.a.createElement(X,null,e("Answer",{initialValue:"",rules:[{required:!0,message:"\u4e0d\u53ef\u4ee5\u5b58\u5728\u7a7a\u7684\u7b54\u6848"}]})(l.a.createElement(V.a,{placeholder:"\u8bf7\u8f93\u5165\u6b63\u786e\u7b54\u6848",onChange:this.onAnswerChange}))),l.a.createElement(X,null,l.a.createElement("br",null),l.a.createElement(A.a,{icon:"upload",type:"primary",loading:this.state.loading,onClick:this.enterLoading},"\u4e0a\u4f20")))))}}]),t}(l.a.Component)),_=B.a.create()(Z),ee=B.a.Item,te=(x.a.Group,function(e){function t(){var e,a;Object(s.a)(this,t);for(var n=arguments.length,l=new Array(n),r=0;r<n;r++)l[r]=arguments[r];return(a=Object(m.a)(this,(e=Object(h.a)(t)).call.apply(e,[this].concat(l)))).state={title:"",answer:"",Unit:"",Qid:""},a.onTitleChange=function(e){a.setState({title:e.target.value})},a.onQidChange=function(e){a.setState({Qid:e.target.value})},a.onAnswerChange=function(e){a.setState({answer:e.target.value})},a.onUnitChange=function(e){a.setState({Unit:e.target.value})},a.enterLoading=function(){a.props.form.getFieldsValue();a.props.form.validateFields(function(e,t){if(!e)F.a.post("http://localhost:8000/request/calculate",M.a.stringify({title:a.state.title,Unit:a.state.Unit,answer:a.state.answer,qid:a.state.Qid})).then(function(e){"114514"==e.data?D.a.success("\u4e0a\u4f20\u6210\u529f!"):D.a.error("\u4e0a\u4f20\u5931\u8d25!!")})})},a.closeLoading=function(){a.setState({loading:!1})},a}return Object(d.a)(t,e),Object(u.a)(t,[{key:"render",value:function(){var e=this.props.form.getFieldDecorator;return l.a.createElement("div",null,l.a.createElement(W.a,{title:"\u8ba1\u7b97\u9898"},l.a.createElement(B.a,null,l.a.createElement(ee,null,e("question",{initialValue:"",rules:[{required:!0,message:"\u4e0d\u53ef\u4ee5\u5b58\u5728\u7a7a\u7684\u9898\u76ee"}]})(l.a.createElement(V.a,{placeholder:"\u8bf7\u8f93\u5165\u9898\u5e72",onChange:this.onTitleChange}))),l.a.createElement(ee,null,e("Unit",{initialValue:"",rules:[{required:!0,message:"\u4e0d\u53ef\u4ee5\u5b58\u5728\u7a7a\u7684\u6240\u5c5e\u5355\u5143"}]})(l.a.createElement(V.a,{placeholder:"\u8bf7\u8f93\u5165\u6240\u5c5e\u5355\u5143",onChange:this.onUnitChange}))),l.a.createElement(ee,null,e("Qid",{initialValue:"",rules:[{required:!0,message:"\u4e0d\u53ef\u4ee5\u5b58\u5728\u7a7a\u7684\u9898\u53f7"}]})(l.a.createElement(V.a,{placeholder:"\u8bf7\u8f93\u5165\u9898\u53f7",onChange:this.onQidChange}))),l.a.createElement(ee,null,l.a.createElement("p",null,"\u6b63\u786e\u7b54\u6848\uff1a")),l.a.createElement(ee,null,e("Answer",{initialValue:"",rules:[{required:!0,message:"\u4e0d\u53ef\u4ee5\u5b58\u5728\u7a7a\u7684\u7b54\u6848"}]})(l.a.createElement(V.a,{placeholder:"\u8bf7\u8f93\u5165\u6b63\u786e\u7b54\u6848",onChange:this.onAnswerChange}))),l.a.createElement(ee,null,l.a.createElement("br",null),l.a.createElement(A.a,{icon:"upload",type:"primary",loading:this.state.loading,onClick:this.enterLoading},"\u4e0a\u4f20")))))}}]),t}(l.a.Component)),ae=B.a.create()(te),ne=B.a.Item,le=(x.a.Group,function(e){function t(){var e,a;Object(s.a)(this,t);for(var n=arguments.length,l=new Array(n),r=0;r<n;r++)l[r]=arguments[r];return(a=Object(m.a)(this,(e=Object(h.a)(t)).call.apply(e,[this].concat(l)))).state={title:"",answer:"",Unit:"",Qid:""},a.onTitleChange=function(e){a.setState({title:e.target.value})},a.onQidChange=function(e){a.setState({Qid:e.target.value})},a.onAnswerChange=function(e){a.setState({answer:e.target.value})},a.onUnitChange=function(e){a.setState({Unit:e.target.value})},a.enterLoading=function(){a.props.form.getFieldsValue();a.props.form.validateFields(function(e,t){if(!e)F.a.post("http://localhost:8000/request/shortanswer",M.a.stringify({title:a.state.title,Unit:a.state.Unit,answer:a.state.answer,qid:a.state.Qid})).then(function(e){"114514"==e.data?D.a.success("\u4e0a\u4f20\u6210\u529f!"):D.a.error("\u4e0a\u4f20\u5931\u8d25!!")})})},a.closeLoading=function(){a.setState({loading:!1})},a}return Object(d.a)(t,e),Object(u.a)(t,[{key:"render",value:function(){var e=this.props.form.getFieldDecorator;return l.a.createElement("div",null,l.a.createElement(W.a,{title:"\u7b80\u7b54\u9898"},l.a.createElement(B.a,null,l.a.createElement(ne,null,e("question",{initialValue:"",rules:[{required:!0,message:"\u4e0d\u53ef\u4ee5\u5b58\u5728\u7a7a\u7684\u9898\u76ee"}]})(l.a.createElement(V.a,{placeholder:"\u8bf7\u8f93\u5165\u9898\u5e72",onChange:this.onTitleChange}))),l.a.createElement(ne,null,e("Unit",{initialValue:"",rules:[{required:!0,message:"\u4e0d\u53ef\u4ee5\u5b58\u5728\u7a7a\u7684\u6240\u5c5e\u5355\u5143"}]})(l.a.createElement(V.a,{placeholder:"\u8bf7\u8f93\u5165\u6240\u5c5e\u5355\u5143",onChange:this.onUnitChange}))),l.a.createElement(ne,null,e("Qid",{initialValue:"",rules:[{required:!0,message:"\u4e0d\u53ef\u4ee5\u5b58\u5728\u7a7a\u7684\u9898\u53f7"}]})(l.a.createElement(V.a,{placeholder:"\u8bf7\u8f93\u5165\u9898\u53f7",onChange:this.onQidChange}))),l.a.createElement(ne,null,l.a.createElement("p",null,"\u6b63\u786e\u7b54\u6848\uff1a")),l.a.createElement(ne,null,e("Answer",{initialValue:"",rules:[{required:!0,message:"\u4e0d\u53ef\u4ee5\u5b58\u5728\u7a7a\u7684\u7b54\u6848"}]})(l.a.createElement(V.a,{placeholder:"\u8bf7\u8f93\u5165\u6b63\u786e\u7b54\u6848",onChange:this.onAnswerChange}))),l.a.createElement(ne,null,l.a.createElement("br",null),l.a.createElement(A.a,{icon:"upload",type:"primary",loading:this.state.loading,onClick:this.enterLoading},"\u4e0a\u4f20")))))}}]),t}(l.a.Component)),re=B.a.create()(le),ie=(a(382),function(e){function t(){var e,a;Object(s.a)(this,t);for(var n=arguments.length,l=new Array(n),r=0;r<n;r++)l[r]=arguments[r];return(a=Object(m.a)(this,(e=Object(h.a)(t)).call.apply(e,[this].concat(l)))).Idelete=function(e){F.a.post("http://localhost:8000/delete",M.a.stringify({id:e})).then(function(e){"114514"==e.data?(a.setState({title:""}),D.a.success("\u5220\u9664\u6210\u529f!")):D.a.error("\u5220\u9664\u5931\u8d25!!")})},a.state={title:"",next:"",id:"",my:""},a}return Object(d.a)(t,e),Object(u.a)(t,[{key:"componentWillMount",value:function(){var e=this;F.a.post("http://localhost:8000/choice",M.a.stringify({title:this.state.title})).then(function(t){""!=t.data?(e.state.my=t.data,D.a.success("\u83b7\u53d6\u6210\u529f!")):D.a.error("\u83b7\u53d6\u5931\u8d25!!")})}},{key:"render",value:function(){return l.a.createElement("div",{className:"homepage"},l.a.createElement(W.a,{title:"\u9009\u62e9\u9898",className:"iquestion"},l.a.createElement(c.a,null,l.a.createElement(o.a,{span:"18"},l.a.createElement("p",{"v-for":"my in my"},this.state.my.title)),l.a.createElement(o.a,{span:"3"},l.a.createElement("div",{className:"ibutton1"},l.a.createElement(v.a,{to:"./detail/choice"},l.a.createElement(A.a,{icon:"edit",type:"primary"},"\u66f4\u6539")))),l.a.createElement(o.a,{span:"3"},l.a.createElement("div",{className:"ibutton2"},l.a.createElement(A.a,{icon:"delete",type:"danger",onClick:this.Idelete(this.state.my.id)},"\u5220\u9664"))))))}}]),t}(l.a.Component)),ce=a(165),oe=a.n(ce),se=a(166),ue=a.n(se),me=a(167),he=a.n(me),de=function(e){function t(){return Object(s.a)(this,t),Object(m.a)(this,Object(h.a)(t).apply(this,arguments))}return Object(d.a)(t,e),Object(u.a)(t,[{key:"render",value:function(){return l.a.createElement(k.a,null,l.a.createElement(N,null,l.a.createElement(q.a,{path:"/admin",render:function(){return l.a.createElement(w,null,l.a.createElement(S.a,null,l.a.createElement(q.a,{exact:!0,path:"/admin",component:O}),l.a.createElement(q.a,{exact:!0,path:"/admin/paper/makepaper",component:Y}),l.a.createElement(q.a,{exact:!0,path:"/admin/paper/history",component:G}),l.a.createElement(q.a,{exact:!0,path:"/admin/question/upload",component:J}),l.a.createElement(q.a,{exact:!0,path:"/admin/question/manage",component:R}),l.a.createElement(q.a,{exact:!0,path:"/admin/question/questions",component:H}),l.a.createElement(q.a,{exact:!0,path:"/admin/question/display/choice",component:P}),l.a.createElement(q.a,{exact:!0,path:"/admin/question/display/calculation",component:ae}),l.a.createElement(q.a,{exact:!0,path:"/admin/question/display/blank",component:_}),l.a.createElement(q.a,{exact:!0,path:"/admin/question/display/shortanswer",component:re}),l.a.createElement(q.a,{exact:!0,path:"/admin/question/manage/choice",component:ie}),l.a.createElement(q.a,{exact:!0,path:"/admin/question/manage/calculation",component:ue.a}),l.a.createElement(q.a,{exact:!0,path:"/admin/question/manage/blank",component:oe.a}),l.a.createElement(q.a,{exact:!0,path:"/admin/question/manage/shortanswer",component:he.a})))}})))}}]),t}(l.a.Component);Boolean("localhost"===window.location.hostname||"[::1]"===window.location.hostname||window.location.hostname.match(/^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/));i.a.render(l.a.createElement(de,null),document.getElementById("root")),"serviceWorker"in navigator&&navigator.serviceWorker.ready.then(function(e){e.unregister()})}},[[172,2,1]]]);
//# sourceMappingURL=main.cfb864bd.chunk.js.map